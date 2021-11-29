from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from rest_framework import generics
from .serializers import NoteSerializer
# Create your views here.

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer