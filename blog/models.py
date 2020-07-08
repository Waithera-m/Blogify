from django.db import models
from django.urls import reverse

class Post(models.Model):
    """
    class facilitates the creation of post objects
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:details", kwargs={"pk": self.pk})

   

