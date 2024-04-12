from django.urls import path
from . import views
from trackingApp.views import NoteListView, NoteDetailView, CreateNoteView, CreateTaskView, TaskListView,RegisterView ,LoginView ,LogoutView,TaskDetailView

urlpatterns = [
    path('', views.index, name='index'),  # URL-шлях до головної сторінки
    # інші URL-шляхи тут
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('create-note/', CreateNoteView.as_view(), name='create_note'),
    
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('create-task/', CreateTaskView.as_view(), name='create_task'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('success/', views.success, name='success'),
    path('denied/', views.denied, name='denied'),
]
