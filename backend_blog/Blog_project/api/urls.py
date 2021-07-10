from django.urls import path, include
from post import views as post

app_name = 'api'

urlpatterns = [
    path('create-post', post.CreatePost.as_view()),
    path('all-post-view', post.PostList.as_view()),
    path('create-post-comment', post.CreateComment.as_view()),
    path('post-comment-view/<int:post_id>', post.PostCommentView.as_view()),
    path('Vote-UnVote-Post', post.Vote_UnVote_Post.as_view())

]
