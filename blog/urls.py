from django.urls import path
from blog import views
from blog.views import PostListView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path(
        '<int:year>/<int:month>/<int:day>/<str:slug>', 
        views.post_detail, 
        name='post_detail'
    ),
    path('<int:id>/share/', views.post_share, name='post_share'),
]