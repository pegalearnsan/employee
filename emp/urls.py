from django.contrib import admin
from django.urls import path
from emp import views

admin.site.site_header = "Employee Administration"
admin.site.site_title = "Employee Admin Site"
admin.site.index_title = "Employee Admin"
urlpatterns = [
    path("",views.index, name="index"),
    path('emplist/', views.emplist, name='emplist'),
    path('search/', views.search, name='search'),
    path('nav/', views.nav, name = 'nav'),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name= 'login_user'),
    path('logout_user/', views.logout_user, name= 'logout_user'),
    path("autocomplete_search/",views.autocomplete_search, name = "autocomplete_search"),


]
