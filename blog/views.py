from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class HomePageView(ListView):
  template_name = 'home.html'
  model = Post

class DetailPageView(DetailView):
  template_name = 'post_detail.html'
  model = Post

