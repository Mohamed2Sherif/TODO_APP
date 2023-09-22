from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from .dto import Task
from .models import Task as Taskdb
from .forms import Task_Form,Managers_Task_Form
from .usecases import add_task_to_database
from src.users.usecases import get_the_user_group
from .decorators import  change_task_form
# TODO: Complete the Clean architecture setup
@login_required()
@change_task_form(groups=["Employee"])
def CreateTask(request,*args,**kwargs):
    user = kwargs['user_id']
    if request.method == 'POST':
        form = kwargs['form'](request.POST)

        if form.is_valid():
            if 'user' in form.cleaned_data:
                user = form.cleaned_data["user"]
            cd = form.cleaned_data
            task = Task(title=f"{cd['title']}",
                        details=f"{cd['details']}",
                        deadline=cd['deadline'] ,
                        user = user
                        )
            taskdb = add_task_to_database(task)
            #TODO: add jquey "Task created successfully" message
            return redirect('tasks:taskdetail',pk=taskdb.pk)
    form = kwargs['form']

    return render(request, 'createtask.html', {'form': form})


class ListTask(LoginRequiredMixin, ListView):
    login_url = '/users/login'
    redirect_field_name = "tasks:listtasks"
    model = Taskdb
    template_name = 'listtasks.html'
    context_object_name = 'tasks'


class UpdateTask(LoginRequiredMixin, UpdateView):
    login_url = '/users/login'
    redirect_field_name = "tasks:updatetask"
    model = Taskdb
    fields = ['title', 'details', 'deadline']
    template_name = 'updatetask.html'
    def get_success_url(self):
        task_pk = self.object.pk

        return reverse_lazy("tasks:taskdetail",kwargs={'pk':task_pk})


class TaskDetail(LoginRequiredMixin, DetailView):
    login_url = '/users/login'
    redirect_field_name = "tasks:taskdetail"
    model = Taskdb
    template_name = "taskdetail.html"
    context_object_name = 'task'


class DeleteTask(LoginRequiredMixin, DeleteView):
    login_url = '/users/login'
    redirect_field_name = "tasks:deletetask"
    model = Taskdb
    template_name = 'deletetask.html'
    success_url = reverse_lazy("tasks:listtasks")
