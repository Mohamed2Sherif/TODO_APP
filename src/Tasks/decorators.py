from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps
from .forms import Task_Form , Managers_Task_Form
def change_task_form(groups=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request,*args, **kwargs):
                user = request.user
                if user.groups.filter(name__in=groups).exists():
                    form_class = Task_Form

                else :
                    form_class = Managers_Task_Form
                form = form_class

                kwargs['form'] =form
                kwargs['user_id'] = user.pk
                return view_func(request,*args, **kwargs)

        return wrapper_func
    return decorator

# def list_user_tasks(view_func):
#     @wraps(view_func)
#     def wrapper_func(request, *args, **kwargs):
#
#
#         return view_func(request,*args,**kwargs)