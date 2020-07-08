from django.shortcuts import render, redirect
from blog.models import Post
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from blog.forms import PostForm

def posts_home(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

def create_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:posts_home')
    else:
        form = PostForm()
        context = {
            "form": form,
        }
    return render(request, 'blog/new_post.html', context)

def update_post(request):
    return HttpResponse('<h1>We have posts</h1>')

def delete_post(request):
    return HttpResponse('<h1>We have posts</h1>')

