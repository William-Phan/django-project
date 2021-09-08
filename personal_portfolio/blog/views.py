from django.shortcuts import render

from blog.models import Blog


def blog_home(request):
    blogs = Blog.objects.all().order_by('-created_date')[:2]
    context = {'blogs': blogs}
    return render(request, 'blog/blog_home.html', context)
