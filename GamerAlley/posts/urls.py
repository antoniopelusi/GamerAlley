from django.urls import path
from .views import (
    post_comment_create_and_list_view,
    upvote_downvote_post,
    PostDeleteView,
    PostUpdateView,
    user_post_view,
    tags_post_view,
)

app_name = 'posts'

urlpatterns = [
    path('', post_comment_create_and_list_view, name='main-post-view'),
    path('me/', user_post_view, name='user-post-view'),
    path('tags/<tag>/', tags_post_view, name='tag-post-view'),
    path('upvoted/', upvote_downvote_post, name='upvote-post-view'),
    path('<pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('<pk>/update/', PostUpdateView.as_view(), name='post-update'),
]
