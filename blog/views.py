from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from blog.forms import PostForm
from django.contrib import messages

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
            post = form.save(commit=False)
            post.save()
            messages.success(request, "Post Created Successfully")
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm()
        context = {
            "form": form,
        }
    return render(request, 'blog/new_post.html', context)

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post =form.save(commit=False)
        post.save()
        messages.success(request, "Post Edited Successfully")
        return HttpResponseRedirect(post.get_absolute_url())
    
    context = {
        "form": form,
        "post": post,
    }
    return render(request, 'blog/update.html', context)

def delete_post(request):
    return HttpResponse('<h1>We have posts</h1>')

