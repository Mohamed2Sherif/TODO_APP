from .Dto import User
from .models import User as Userdb
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password


def AddUserToDB(user:User):
    Userdb.objects.create(
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        email=user.email,
        password=make_password(user.password),
        group=user.group
        )
    userdb = Userdb.objects.get(username=user.username)

    if userdb.group == 'MA':
        manager = Group.objects.get(name="Manager")
        userdb.groups.add(manager)
    if userdb.group == 'MO':
        moderator = Group.objects.get(name="Moderator")
        userdb.groups.add(moderator)
    if userdb.group == 'EM':
        employee=Group.objects.get(name="Employee")
        userdb.groups.add(employee)





