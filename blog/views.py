from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic

def posts_home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

def create_post(request):
    return HttpResponse('<h1>We have posts</h1>')

def update_post(request):
    return HttpResponse('<h1>We have posts</h1>')

def delete_post(request):
    return HttpResponse('<h1>We have posts</h1>')

