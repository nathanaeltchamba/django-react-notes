from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializers
from .models import Notes

# Create your views here.
@api_view(['GET'])
def getNotes(request):

    notes = Notes.objects.all()
    serailizer = NoteSerializers(notes, many=True)
    return Response(serailizer.data)

@api_view(['GET'])
def getNote(request, pk):

    notes = Notes.objects.get(id=pk)
    serailizer = NoteSerializers(notes, many=False)
    return Response(serailizer.data)