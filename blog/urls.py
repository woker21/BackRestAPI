from django.urls import path
from .views import BlogViews, BlogViewsDetail

urlpatterns = [
    path('blogapi/', BlogViews.as_view(), name='blog-list'),
    path('blogapi/<int:pk>/', BlogViewsDetail.as_view(), name='blog-datail'),
    
]
