from rest_framework import viewsets, mixins, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny

from posts.models import Post, Group
from .serializers import PostSerializer, CommentSerializer
from .serializers import GroupSerializer, FollowSerializer
from .permissions import OwnerOrReadOnly


class CreateViewSet(viewsets.ModelViewSet):
    permission_classes = (OwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CreateListViewSet(
        mixins.CreateModelMixin, mixins.ListModelMixin,
        viewsets.GenericViewSet):
    pass


class PostViewSet(CreateViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination


class CommentViewSet(CreateViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(pk=post_id)
        return post.comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(pk=post_id)
        serializer.save(post=post, author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.follower
