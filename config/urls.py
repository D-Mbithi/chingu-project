from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'post': PostSitemap
}


urlpatterns = [
    path(
        'design/', 
        TemplateView.as_view(template_name='index.html'), 
        name='index'
    ),
    path('', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path(
        'sitemap.xml', 
        sitemap, 
        {'sitemaps': sitemaps,}, 
        name='django.contribe.sitemaps.views.sitemap'
    )
]
