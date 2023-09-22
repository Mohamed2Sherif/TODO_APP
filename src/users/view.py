from django import forms
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView,UpdateView
from django.contrib.auth import authenticate, login as login_user,logout as logout_user
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .Dto import User
from .usecases import AddUserToDB
from .models import User as Userdb
#TODO:Complete the clean architecture setup


class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=25)
    last_name = forms.CharField(label="Last Name", max_length=25)
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    group = forms.ChoiceField(label="Group",choices=Userdb.Groups.choices)
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)

@login_required()
@permission_required("src_users.add_user",raise_exception=True)
def CreateUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User(username=f"{cd['username']}",
                        email=f"{cd['email']}",
                        first_name=f"{cd['first_name']}",
                        last_name=f"{cd['last_name']}",
                        password=f"{cd['password']}",
                        group=f"{cd['group']}",
                        )
            AddUserToDB(user)

    else:
        form = UserForm()

    return render(request, 'createuser.html', {'form': form})


class ListUsers(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required= ['src_users.change_user','src_users.view_user']
    model = Userdb
    template_name = 'userslist.html'
    context_object_name = 'users'
    login_url = 'users:Login'
    redirect_field_name = 'users:ListUsers'
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'],password=cd['password'])

            if user is not None:
                login_user(request,user)

                return redirect('users:ListUsers')

    form = LoginForm()

    return render(request,'login.html',{'form':form})

def logout(request):
    logout_user(request)

    return redirect('users:Login')


class UserDetails(DetailView):
    model = Userdb
    template_name = 'userdetails.html'
    context_object_name = "user"

class UserUpdate(UpdateView):
    model = Userdb
    template_name = "updateuser.html"
    fields = ["first_name",'last_name', 'email','username']
    context_object_name = "user"
