from django.db import models
from django.conf import settings
from PIL import Image


class Post(models.Model):
    titre = models.CharField(max_length=300)
    sous_titre = models.CharField(max_length=300, blank=True)
    body_post = models.TextField(max_length=50000)
    image = models.ImageField(blank=True, null=True, upload_to=settings.MEDIA_ROOT, verbose_name='images')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Article(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titre_article = models.CharField(max_length=100)
    image_article = models.ImageField(blank=True)
    description_article = models.TextField(max_length=20000000)
    signature = models.CharField(max_length=10)
