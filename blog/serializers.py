from rest_framework import serializers

from blog.models import BlogPost


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'body', 'author_id')