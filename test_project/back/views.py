import os

from django.conf import settings
from rest_framework.viewsets import GenericViewSet, mixins
from back.models import Post
from back.serializers import PostSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class PostViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):

    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def list(self, request, *args, **kwargs):
        instances = self.get_queryset()
        serializer = self.serializer_class(instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Post, pk=self.kwargs['pk'])
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MyPostsViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Post.objects.filter(author__pk=self.request.user.pk)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(Post, pk=self.kwargs['pk'])
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = get_object_or_404(Post, pk=self.kwargs['pk'])
        serializer = self.serializer_class(instance, data=self.request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            if request.data.get('image_b'):
                os.remove(settings.MEDIA_ROOT + str(instance.image_b))
            elif request.data.get('image_s'):
                os.remove(settings.MEDIA_ROOT + str(instance.image_s))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        instance = get_object_or_404(Post, pk=self.kwargs['pk'])
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)