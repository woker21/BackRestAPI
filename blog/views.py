from .models import BlogApi
from .serializer import BlogApiSerializer
from rest_framework import generics


class BlogViews(generics.ListCreateAPIView):
    queryset = BlogApi.objects.all()
    serializer_class = BlogApiSerializer
    
class BlogViewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogApi.objects.all()
    serializer_class = BlogApiSerializer