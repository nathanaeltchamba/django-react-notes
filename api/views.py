from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializers
from .models import Notes
from .utils import updateNote, getNoteDetail, deleteNote, getNotesList, createNote

# Create your views here.
@api_view(['GET'])
def getNotes(request):

    notes = Notes.objects.all().order_by('-updated')
    serailizer = NoteSerializers(notes, many=True)
    return Response(serailizer.data)

# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Notes.objects.create(
#         body=data['body']
#     )
#     serializer = NoteSerializers(note, many=False)
#     return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):

    notes = Notes.objects.get(id=pk)
    serailizer = NoteSerializers(notes, many=False)
    return Response(serailizer.data)

@api_view(['GET', 'POST'])
def getNotes(request):

    if request.method == 'GET':
        return getNotesList(request)

    if request.method == 'POST':
        return createNote(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):

    if request.method == 'GET':
        return getNoteDetail(request, pk)

    if request.method == 'PUT':
        return updateNote(request, pk)

    if request.method == 'DELETE':
        return deleteNote(request, pk)

# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data
#     note = Notes.objects.get(id=pk)
#     serializer = NoteSerializers(instance=note, data=data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['DELETE'])
# def deleteNote(request, pk):
#     note = Notes.objects.get(id=pk)
#     note.delete()
#     return Response('Note was deleted!')