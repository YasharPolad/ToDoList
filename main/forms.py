from django.forms import ModelForm, forms, widgets
from django.contrib.auth.models import User
from .models import Comment, Membership, Task
from django import forms

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'text', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
        }

class ShareForm(ModelForm):
    class Meta:
        model = Membership
        fields = ['user', 'status']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']