from .dto import Task
from .models import Task as Taskdb
from django import forms
from .widgets import DatePickerInput

class Task_Form(forms.ModelForm):
    # TODO: Make the deadline form field accept time and date
    class Meta:
        model = Taskdb
        fields = ['title', 'details', 'deadline']

        widgets = {
            'deadline': DatePickerInput,

        }



class Managers_Task_Form(forms.ModelForm):
    class Meta:
        model = Taskdb
        fields = ['title', 'details', 'deadline','user']

        widgets = {
            'deadline': DatePickerInput
        }