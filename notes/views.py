from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy
from .models import Notes

# Create your views here.
class NotesHomePageView(ListView):
    model = Notes
    template_name = "notes/noteshomepage.html"   
    context_object_name = 'all_notes'

class NotesPageView(DetailView):
    model = Notes
    template_name = 'notes/noteslistpage.html'
    context_object_name = 'notes_detail'

class NotesEditView(UpdateView):
    model = Notes
    template_name = 'notes/noteseditpage.html'
    fields  = ['title', 'body']

class NotesDeleteView(DeleteView):
    model = Notes
    template_name = 'notes/notesdeletepage.html'
    success_url = reverse_lazy("noteshome")

class NotesNewView(CreateView):
    model = Notes
    template_name = 'notes/notesnewpage.html'
    fields = ['title', 'body']

