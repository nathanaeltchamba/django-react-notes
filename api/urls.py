from django.urls import path
from .views import getNotes, getNote


urlpatterns = [
    path('notes/', getNotes, name='notes'),
    # path('notes/<str:pk>/update', updateNote, name='update-note'),

    # path('notes/create/', createNote, name="create-note"),
    # path('notes/<str:pk>/delete/', deleteNote, name="delete-note"),

    path('notes/<str:pk>/', getNote, name='note-detail'),
]