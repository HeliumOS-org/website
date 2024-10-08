from django.core.paginator import Paginator
from django.contrib.sitemaps.views import sitemap
from django_distill import distill_path

from . import views
from .models import BlogPost
from .sitemaps import sitemaps


def get_all_blog_pages():
    all_posts = BlogPost.objects.order_by("create_date")
    paginator = Paginator(all_posts, 10)
    for page_number in paginator.page_range:
        yield {'page_number': page_number}


def get_all_blog_posts():
    all_posts = BlogPost.objects.order_by("create_date")
    for post in all_posts:
        yield {'slug': post.slug}

def get_all_release_lists():
    for type_ in ["pre-release"]:
        yield {'type_': type_}

urlpatterns = [
    distill_path("", views.index, name="index"),
    distill_path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    distill_path("download/", views.download, name="download"),
    distill_path("blog/", views.blog, name="blog"),
    distill_path("blog/page/<int:page_number>/", views.blog, name="blog", distill_func=get_all_blog_pages),
    distill_path("blog/post/<str:slug>/", views.blog_post, name='blog_post', distill_func=get_all_blog_posts),
    distill_path("feed.xml", views.BlogFeed(), name="feed"),
    distill_path("releases/<str:type_>/", views.release_list, name="release_list", distill_func=get_all_release_lists),
    distill_path("docs/", views.docs, name="docs"),
    distill_path("roadmap/", views.roadmap, name="roadmap"),
    distill_path("hardware/", views.hardware, name="hardware"),
]
