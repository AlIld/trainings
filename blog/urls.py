from django.urls import path
from blog.views import(
    create_blog_view,
    detail_blog_view,
    edit_blog_view,
    ArticleView,
    SingleArticleView,
)

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_view, name="create"),
    path('api/', ArticleView.as_view(), name="api"),
    path('api/<int:pk>', SingleArticleView.as_view(), name="single_api"),
    path('<slug>/', detail_blog_view, name="detail"),
    path('<slug>/edit', edit_blog_view, name="edit"),
]