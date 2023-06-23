from django.shortcuts import render

from .models import Post
from django.views.generic import ListView

# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'all_task'
