from django.urls import path, re_path
from blog.views import (
    create_blog_view,
    detail_blog_view,
    edit_blog_view,
    ArticleView,
    SingleArticleView,
    schema_view)

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_view, name="create"),
    path('api/', ArticleView.as_view(), name="api"),
    path('api/<int:pk>', SingleArticleView.as_view(), name="single_api"),
    re_path(r'^swagger', schema_view, name="swagger"),
    path('<slug>/', detail_blog_view, name="detail"),
    path('<slug>/edit', edit_blog_view, name="edit"),
]