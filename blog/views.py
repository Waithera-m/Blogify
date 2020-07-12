from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from blog.forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger
from urllib.parse import quote_plus
from django.utils import timezone
from django.db.models import Q

def posts_home(request):
    """
    view function gets post saved in teh database
    """
    posts_list = Post.objects.active().order_by('-id')
    if request.user.is_superuser or request.user.is_staff:
        posts_list = Post.objects.all().order_by('-id')
    
    query = request.GET.get("q")
    if query:
        posts_list = posts_list.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(user__username__icontains=query)).distinct()
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    context = {
        'posts':posts,
        
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, slug=None):
    """
    view function gets a single post associated with the passed unique slug
    """
    post = get_object_or_404(Post, slug=slug)
    if post.draft:
        if not request.user.is_authenticated or not request.user.is_superuser:
            raise Http404
    elif post.publish>timezone.now().date():
        if not request.user.is_authenticated or not request.user.is_superuser:
            raise Http404
        
    string_share = quote_plus(post.content)
    context = {
        'post': post,
        'string_share': string_share,
    }
    return render(request, 'blog/detail.html', context)

def create_post(request):
    """
    view function handles the creation of new post instances
    """
    if not request.user.is_authenticated:
        raise Http404
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
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
    """
    view function uodates a single post
    """
    if not request.user.is_authenticated:
        raise Http404
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
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

def delete_post(request, pk):
    """
    view function handles the deletion of a single post
    """
    if not request.user.is_authenticated:
        raise Http404
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, "Post Deleted Successfully")
    return redirect('blog:posts_home')

