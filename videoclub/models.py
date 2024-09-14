from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=250)
    subTitle = models.CharField(max_length=250)
    enlace = models.CharField(max_length=50)
        
class Like(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="likes")
    create_date = models.DateTimeField(auto_now_add=False) 