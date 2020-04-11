from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from posts.models import Post, Comments

def posts(request):
    return render(request,'posts/all_posts.html', context={'posts': Post.objects.all()})

def post(request, post_id=1):
    return render(request,'posts/one_post.html', context={'post': Post.objects.get(id=post_id), 'comments': Comments.objects.filter(comments_post_id=post_id)})
