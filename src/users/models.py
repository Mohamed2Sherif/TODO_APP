from django.db import models
from django.contrib.auth.models import (
            BaseUserManager,
            AbstractBaseUser,
            PermissionsMixin)
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,username,password,*args,**kwargs):
        if email is None : raise TypeError("please provide an email address")
        if username is None : raise TypeError("please provide a username")
        if password is None : raise TypeError("please provide a password")

        user = self.model(email=self.normalize_email(email),username=username,**kwargs)
        user.set_password(password)
        user.save(using=self.db)

        return user
    def create_superuser(self,email,username,password=None,**kwargs):
        if email is None : raise TypeError("please provide an email")
        if username is None : raise TypeError("please provide a username")
        if password is None : raise TypeError("please provide a password")

        user = self.create_user(email,username,password,**kwargs)
        user.is_superuser = True
        user.is_staff =True
        user.save(using=self.db)

        return user
class User(AbstractBaseUser,PermissionsMixin):

    class Groups(models.TextChoices):
        Employee = "EM","Employee"
        Moderator = "MO","Moderator"
        Manager = "MA", "Manager"

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True,db_index=True,)
    username = models.CharField(max_length=100,unique=True,db_index=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    group = models.CharField(max_length=2,choices=Groups.choices,default=Groups.Employee)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return f'{self.email}'
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

