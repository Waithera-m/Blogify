from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

def posts_home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def get_single_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except ObjectDoesNotExist:
        pass
    return render(request, 'blog/detail.html', {'post':post})
    


def create_post(request):
    return HttpResponse('<h1>We have posts</h1>')

def update_post(request):
    return HttpResponse('<h1>We have posts</h1>')

def delete_post(request):
    return HttpResponse('<h1>We have posts</h1>')

