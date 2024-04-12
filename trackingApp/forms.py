from django import forms
from trackingApp.models import Task, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description","status","priority","due_date"]


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']