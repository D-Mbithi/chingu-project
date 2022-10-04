from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('design/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]
