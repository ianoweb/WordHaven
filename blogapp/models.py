from django.db import models
from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.

class categories(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = RichTextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads')
    url = models.SlugField(unique=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(categories, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    is_approved = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

