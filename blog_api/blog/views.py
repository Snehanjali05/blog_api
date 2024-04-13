# from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions
from rest_framework.routers import DefaultRouter

from .models import Post
from blog.serializers import PostSerializer
from blog.permissions import IsAuthorOrReadOnly

# Create your views here.

class PostViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,\
                  mixins.RetrieveModelMixin, mixins.UpdateModelMixin,\
                  mixins.DestroyModelMixin,GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    
    def get_serializer_class(self):
        return super().get_serializer_class()

router = DefaultRouter()
router.register("post", PostViewSet, "post")

