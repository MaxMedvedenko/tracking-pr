from django.shortcuts import render, redirect

from django.views.generic import ListView
from .models import Note

from django.views.generic import DetailView

from django import forms

from django.views import View
from django.http import HttpResponse
#from .forms import NoteForm#

# Create your views here.

def index(request):
    return render(request, 'trackingApp/index.html')

class NoteListView(ListView):
    model = Note
    template_name = 'trackingApp/note_list.html'
    context_object_name = 'notes'


from django.views.generic import DetailView
from .models import Note

class NoteDetailView(DetailView):
    model = Note
    template_name = 'trackingApp/note_detail.html'
    context_object_name = 'note'

from django import forms
from .models import Note

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
            # Обробка валідних даних форми та збереження нової замітки
            return HttpResponse("Замітка успішно створена!")
        else:
            return render(request, 'trackingApp/create_note.html', {'form': form})