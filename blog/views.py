from django.shortcuts import render, get_object_or_404
from blog.models import Comment, Post
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.core.mail import send_mail

from .forms import EmailPostForm, CommentForm

# Create class base views
class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = "blog/list.html"


# # Create your views here.
# def post_list(request):
#     post_list = Post.published.all()
#     categories = Category.objects.all()
#     paginator = Paginator(post_list, 3)
#     page_number = request.GET.get('page', 1)
# 
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
# 
#     template =  'blog/list.html'
#     context = {
#         'posts': posts,
#         'categories': categories
#     }
# 
#     return render(request, template, context)

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=slug,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        )
    comments = post.comments.filter(active=True)
    form = CommentForm()
    template = 'blog/detail.html'
    context = {
        'post': post,
        'form': form,
        'comments': comments
    }

    return render(request, template, context)


def post_share(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == "POST":
        form = EmailPostForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = f"{cd['name']}recommends you read {post.title}."
            message = f"Read {post.title} at {post_url} \n\n {cd['name']}'s comments: {cd['comments']}"
            send_mail(subject, message, 'denniswamumbua@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    template = "blog/share.html"
    context = {
        'post': post,
        'form': form,
        'sent': sent
    }

    return render(request, template, context)


@require_POST
def post_comment(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    comment = None

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    
    template = 'blog/comment.html'
    context = {
        'form': form,
        'post': post,
        'comment': comment
    }

    return render(request, template, context)