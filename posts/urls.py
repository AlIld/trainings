from django.conf.urls import url, include
from posts import views
import posts

urlpatterns = (
    url(r'posts/all/$', posts.views.posts, name='all_post'),
    url(r"posts/get/(?P<post_id>\d+)/$", posts.views.post, name='one_posts'),
)