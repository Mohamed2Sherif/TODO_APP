from django.urls import path
from .views import *

app_name = 'tasks'

urlpatterns =[
    path('create/',CreateTask,name='createtask'),
    path('',ListTask.as_view(),name='listtasks'),
    path('update/<int:pk>',UpdateTask.as_view(),name='updatetask'),
    path('detail/<int:pk>',TaskDetail.as_view(),name='taskdetail'),
    path('delete/<int:pk>',DeleteTask.as_view(),name='deletetask'),
]