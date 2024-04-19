from django.urls import path
from . import views
from trackingApp.views import NoteListView, NoteDetailView, CreateNoteView, CreateTaskView, TaskListView,RegisterView ,LoginView ,LogoutView,TaskDetailView, TaskUpdateView, TaskDeleteView, AddCommentToTaskView

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

    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),

    path('tasks/<int:pk>/add-comment/', AddCommentToTaskView.as_view(), name='add_comment'),

    path('success/', views.success, name='success'),
    path('denied/', views.denied, name='denied'),
]
