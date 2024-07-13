# notes/urls.py

from django.urls import path
from .views import NoteListCreate, NoteRetrieveUpdateDestroy

urlpatterns = [
    path('notes/', NoteListCreate.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroy.as_view(), name='note-detail'),
]
