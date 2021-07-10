from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import UserProfile
from rest_framework.views import APIView
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets, permissions, status
from .models import Post, Comment, Vote


# Create your views here.


class CreatePost(APIView):

    def post(self, request):

        try:
            post_data = self.request.data
            # post_data['author'] = request.user.id
            post_data['author'] = UserProfile.objects.filter(user=request.user).values_list('id', flat=True)[0]

            # UserProfile.objects.filter(user=request.user).values_list('user_id', flat=True)[0]
            serializer_post_data = PostSerializer(data=post_data)
            if serializer_post_data.is_valid(raise_exception=True):
                post_data_saved = serializer_post_data.save()
                return Response({'status': True, 'massage': 'Post created Successfully'})
            return Response({'status': False, 'massage': 'Something is Wrong'})
        except Exception as e:
            print(e)
            return Response({'status': False, 'massage': 'Something is Wrong'})


class PostList(APIView):
    def get(self, request, format=None):
        try:
            queryset = Post.objects.all()
            serializer_data = PostSerializer(queryset, many=True)
            return Response(serializer_data.data)
        except Exception as e:
            return Response({'status': False, 'error': 'Something is Wrong'})


class CreateComment(APIView):
    def post(self, request):
        try:
            post_instance = Post.objects.filter(id=request.data['post_id']).values_list('id')[0]
            request.data['post'] = post_instance[0]
            request.data['user'] = UserProfile.objects.filter(user=request.user).values_list('id', flat=True)[0]
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostCommentView(APIView):

    def get(self, request, **kwargs):
        try:
            comment_data = Comment.objects.filter(post_id=self.kwargs['post_id'])
            serilizer_data = CommentSerializer(comment_data, many=True)
            return Response(serilizer_data.data)
        except Exception as e:

            return Response(serilizer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class Vote_UnVote_Post(APIView):
    def post(self, request):
        try:
            post_id = request.data['post_id']
            post_obj = Post.objects.get(id=post_id)
            profile = UserProfile.objects.get(user=request.user)
            profile_id = UserProfile.objects.filter(user=request.user).values_list('id', flat=True)[0]

            if profile in post_obj.vote_post.all():
                post_obj.vote.remove(profile_id)
            else:
                post_obj.vote_post.add(profile_id)

            vote, created = Vote.objects.get_or_create(user=profile, post_id=post_id)

            if not created:
                if vote.value == 'upvote':
                    vote.value = 'downvote'
                else:
                    vote.value = 'upvote'
            else:
                vote.value = 'upvote'

                post_obj.save()
                vote.save()

            data = {
                'value': vote.value,
                'likes': post_obj.vote_post.all().count()
            }

            return Response(data)
        except Exception as e:
            print(e)
