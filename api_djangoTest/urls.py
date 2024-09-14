from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/videoclub/', include('videoclub.urls')),
    path('api/blog/', include('blog.urls')),
]
