from rest_framework import serializers
from .models import BlogApi

class BlogApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogApi
        fields = "__all__"