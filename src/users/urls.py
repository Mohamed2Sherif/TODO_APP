from django.urls import path

from .view import *
app_name = 'users'
urlpatterns =[
    path('',ListUsers.as_view(),name='ListUsers'),
    path('create/',CreateUser,name='UserCreation'),
    path('login/',login,name='Login'),
    path('logout/',logout,name='Logout'),
]