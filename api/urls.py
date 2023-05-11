from django.urls import path
from .views import getNotes, getNote


urlpatterns = [
    path('notes/', getNotes),
    path('notes/<str:pk>/', getNote)
]