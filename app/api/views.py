from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from app.api.serializers import CreatorSerializer, PostSerializer, CommentSerializer, CategorySerializer, \
    PostViewCountSerializer
from app.models import Creator, Post, Comment, Category, PostViewCount


class CreatorView(ModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self.broadcast('creator_created', CreatorSerializer(instance).data)

    def perform_update(self, serializer):
        instance = serializer.save()
        self.broadcast('creator_updated', CreatorSerializer(instance).data)

    def broadcast(self, event, data):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications", {"type": "send_notification", "event": event, "data": data}
        )


class PostView(ModelViewSet):
    queryset = Post.objects.select_related('creator').prefetch_related('comments', 'categories')
    serializer_class = PostSerializer


class CommentView(ModelViewSet):
    queryset = Comment.objects.select_related('post', 'creator')
    serializer_class = CommentSerializer
    filterset_fields = ['post', 'creator']


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewCountView(APIView):
    def post(self, request, pk):
        session_id = request.session.session_key or request.session.save() or request.session.session_key
        post = Post.objects.get(pk=pk)
        PostViewCount.objects.create(post=post, viewer_session=session_id)
        return Response({'status': 'view count added'})
