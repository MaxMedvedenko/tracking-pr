from django.urls import path
from . import views
from trackingApp.views import NoteListView, NoteDetailView, CreateNoteView
urlpatterns = [
    path('', NoteListView.as_view(), name='home'),  # URL-шлях до головної сторінки
    # інші URL-шляхи тут
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('notes/create/', CreateNoteView.as_view(), name='create_note'),
]
