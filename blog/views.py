from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Post
from .serializers import PostSerializers


class PostListView(ListAPIView):
    queryset = Post.objects.all()[:3]
    serializer_class = PostSerializers

class PostListView2(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostCreateListView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers