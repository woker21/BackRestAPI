from django.db import models

class BlogApi(models.Model):
    title_comment = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    cration_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True)
    
class Answer(models.Model):
    blog_post = models.ForeignKey(BlogApi, on_delete=models.CASCADE, related_name="answers")
    create_date = models.DateField(auto_now_add=False)