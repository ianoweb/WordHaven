from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blogs, categories, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def blog(request):
    approved_blogs = Blogs.objects.filter(is_published=True)
    blog_categories = categories.objects.annotate(blog_count=models.Count('blogs'))
    recent_posts = Blogs.objects.order_by('-date')[:5]
    for blog in approved_blogs:
        blog.comment_count = blog.comment_set.filter(is_approved=True).count()

    blogs_per_page = 1
    paginator = Paginator(approved_blogs, blogs_per_page)

    page_number = request.GET.get('page')
    blogpaginator = paginator.get_page(page_number)

    context = {'blogs': blogpaginator, 'blog_categories': blog_categories, 'recent_posts': recent_posts}

    return render(request, 'blog.html', context)


def post_detail(request, url):
    post = get_object_or_404(Blogs, url=url)
    approved_blogs = Blogs.objects.filter(is_published=True)
    blog_categories = categories.objects.annotate(blog_count=models.Count('blogs'))
    # recent blogs
    recent_posts = Blogs.objects.order_by('-date')[:5]
    comments = post.comment_set.filter(is_approved=True)
    for blog in approved_blogs:
        blog.comment_count = blog.comment_set.filter(is_approved=True).count()

    context = {'post': post, 'blogs': approved_blogs, 'blog_categories': blog_categories, 'recent_posts': recent_posts,
               'comments': comments}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        comment_instance = Comment(name=name, email=email, message=message, blog=post)
        comment_instance.save()
        return redirect('postdetail', url=url)
    return render(request, 'blog_details.html', context)


def search(request):
    if request.method == 'POST':
        search_content = request.POST['name']
        results = Blogs.objects.filter(Q(is_published=True) & Q(title__icontains=search_content))
        # results = Blogs.objects.filter(is_published=True)
        blog_categories = categories.objects.annotate(blog_count=models.Count('blogs'))
        recent_posts = Blogs.objects.order_by('-date')[:5]
        for blog in results:
            blog.comment_count = blog.comment_set.filter(is_approved=True).count()

        blogs_per_page = 1
        paginator = Paginator(results, blogs_per_page)

        page_number = request.GET.get('page')
        blogpaginator = paginator.get_page(page_number)

    context = {'blogs': blogpaginator, 'blog_categories': blog_categories, 'recent_posts': recent_posts}
    return render(request, 'blog.html', context)