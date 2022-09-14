from django.shortcuts import render
from blog.models import Post

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    template =  'blog/list.html'
    context = {
        'posts': posts
    }

    return render(request, template, context)


def post_detail(request, pk):
    post = Post.published.get(pk=pk)
    template = 'blog/detail.html'
    context = {
        'post': post
    }

    return render(request, template, context)