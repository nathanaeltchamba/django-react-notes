from rest_framework.response import Response
from .models import Notes
from .serializers import NoteSerializers


def getNotesList(request):
    notes = Notes.objects.all().order_by('-updated')
    serializer = NoteSerializers(notes, many=True)
    return Response(serializer.data)


def getNoteDetail(request, pk):
    notes = Notes.objects.get(id=pk)
    serializer = NoteSerializers(notes, many=False)
    return Response(serializer.data)


def createNote(request):
    data = request.data
    note = Notes.objects.create(
        body=data['body']
    )
    serializer = NoteSerializers(note, many=False)
    return Response(serializer.data)

def updateNote(request, pk):
    data = request.data
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializers(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteNote(request, pk):
    note = Notes.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')