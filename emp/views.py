from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from emp.models import Employee
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .forms import UserForm
from django.http import JsonResponse

# Create your views here.
@login_required
def index(request):

    if request.method=="POST":
        if request.POST.get('name') and request.POST.get('phone'):
            employee = Employee()

            employee.name = request.POST.get('name')
            employee.phone = request.POST.get('phone')

            employee.save()
        return render(request, "index.html")
    else:
        return render(request, "index.html")



@login_required
def emplist(request):
    employee_list = Employee.objects.order_by("name")
    empdict= {'employees':employee_list}
    return render(request, 'emplist.html',context = empdict)

@login_required
def search(request):
    if request.method=='POST':
        searched = request.POST.get('searched')
        empl = Employee.objects.filter(name__icontains = searched)
        return render(request, "search.html",{'searched':searched, 'empl':empl})
    else:
        return render(request, "search.html")


@login_required
def nav(request):
    return render(request, 'nav.html')


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST)


        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()


            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'register.html',
                                        {'user_form':user_form,
                                            'registered':registered})





def login_user(request):

    if request.method == "POST":
        username = request.POST.get("login_username")
        password = request.POST.get("login_password")

        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect("index")
            else:
                return HttpResponse('Account Not Active')
        else:
             return HttpResponse("Invalid Login Details!")


    else:
        return render (request, 'login_user.html')

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def autocomplete_search(request):
    query = request.GET.get('name', '')
    queryset = Employee.objects.filter(name__icontains=query)[:10]
    results = [m.name for m in queryset]
    return JsonResponse(results, safe=False)
