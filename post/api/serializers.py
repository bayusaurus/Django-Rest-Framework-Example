from post.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=20, max_length=200)
    content = serializers.CharField(min_length=200,)
    category = serializers.CharField(min_length=3, max_length=100)
    class Meta:
        model = Post
        fields = '__all__'