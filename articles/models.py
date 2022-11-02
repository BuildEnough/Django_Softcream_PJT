from django.db import models
from django.conf import settings
# from imagekit.processors import ProcessedImageField
# from imagekit.processors import Thumbnail
# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/',
        blank=True,
      	# processors=[Thumbnail(630,630)],
      	# format="JPEG",
      	# options={'quality' : 90},
        )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

class Comment(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# class Image(models.Model):
#     article = models.ForeignKey(Articles, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='image', blank=True, null=True)