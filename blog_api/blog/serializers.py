from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'created_at', 'updated_at']
        fields_read_only = ['id', 'created_at', 'updated_at']

class PostSerializer(BaseSerializer):
    class Meta:
        model = Post
        fields = BaseSerializer.Meta.fields + ['title', 'content', 'author']
        
    def to_internal_value(self,instance):
        print(instance)
        return super().to_internal_value(instance)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = rep.get('author')
        user = User.objects.get(id=author)
        rep['author']= {'id':user.id, 'name':user.username}
        return rep