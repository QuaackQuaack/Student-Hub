from django.shortcuts import render

from .models import Post
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'all_task'

class NotesDetailView(DetailView):
    template_name = 'todolist.html'
    model = Post
    context_object_name = 'taskdetail'

class CreatePageView(CreateView):
    template_name = 'newtodolist.html'
    fields = ['task', 'body']
    model = Post

class DeletePageView(DeleteView):
    template_name = 'deletetodolist.html'
    model = Post
    success_url = reverse_lazy("home")

class UpdatePageView(UpdateView):
    template_name = 'updatetodolist.html'
    model  = Post
    fields = ['task', 'body' ] 
    

