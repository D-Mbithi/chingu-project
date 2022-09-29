from django.urls import path
from blog import views
# from blog.views import PostListView

app_name = 'blog'

urlpatterns = [
    # path('', PostListView.as_view(), name='post_list'),
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>', views.post_list, name='post_list_by_tag'),
    path(
        '<int:year>/<int:month>/<int:day>/<str:slug>', 
        views.post_detail, name='post_detail'
    ),
    path('<int:id>/share/', views.post_share, name='post_share'),
    path('<int:id>/comment/', views.post_comment, name='post_comment'),
]