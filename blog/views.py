from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def post_list(request):
    post_list = Post.published.all()
    categories = Category.objects.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    template =  'blog/list.html'
    context = {
        'posts': posts,
        'categories': categories
    }

    return render(request, template, context)


def post_detail(request, year, month, day, slug):
    print(year, month, day, slug)
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=slug,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        )
    template = 'blog/detail.html'
    context = {
        'post': post
    }

    return render(request, template, context)