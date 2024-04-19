from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView

from django import forms
from trackingApp.forms import TaskForm, UserRegistrationForm, UserLoginForm, TaskUpdateForm, CommentForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic.base import RedirectView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404

from trackingApp.models import *
# Create your views here.
def index(request):
    return render(request, 'trackingApp/index.html')

class CheckUserInSessionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('denied'))
        return super().handle_no_permission()
    
class TaskListView(ListView):
    model = Task
    template_name = 'trackingApp/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'trackingApp/task_detail.html'
    context_object_name = 'task'

class NoteListView(ListView):
    model = Note
    template_name = 'trackingApp/note_list.html'
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'trackingApp/note_detail.html'
    context_object_name = 'note'

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'trackingApp/create_note.html', {'form': form})

class CreateNoteView(View):
    def get(self, request):
        form = NoteForm()
        return render(request, 'trackingApp/create_note.html', {'form': form})

    def post(self, request):
        form = NoteForm(request.POST)
        if form.is_valid():
            return HttpResponse("Замітка успішно створена!")
        else:
            return render(request, 'trackingApp/create_note.html', {'form': form})



class CreateTaskView(CheckUserInSessionMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'trackingApp/create_task.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

# register, login, logout #
class RegisterView(FormView):
    template_name = 'trackingApp/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        auth_login(self.request, user)
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'trackingApp/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return super().form_valid(form)

class LogoutView(RedirectView):
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super().get(request, *args, **kwargs)

def success(request):
    return render(request, 'trackingApp/success.html')

def denied(request):
    return render(request, 'trackingApp/denied.html')



# Функція перевірки, чи є користувач автором задачі або суперкористувачем
def is_creator_or_superuser(user, task):
    return user.is_superuser or user == task.creator

# Клас для перевірки користувача перед видаленням або редагуванням завдання
class CheckTaskPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        task = self.get_object()
        return is_creator_or_superuser(self.request.user, task)

# Клас для редагування завдання
class TaskUpdateView(CheckTaskPermissionMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'trackingApp/task_update_form.html'
    success_url = reverse_lazy('success')

# Клас для видалення завдання
class TaskDeleteView(CheckTaskPermissionMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('success')



class AddCommentToTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
        return redirect('task_detail', pk=pk)

    def get(self, request, pk):
        return redirect('task_detail', pk=pk)