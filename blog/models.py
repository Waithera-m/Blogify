from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Post(models.Model):
    """
    class facilitates the creation of post objects
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True, width_field="width_field", height_field="height_field", upload_to='images/')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:details", kwargs={"slug": self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    querystring = Post.objects.filter(slug=slug).order_by('-pk')
    exists = querystring.exists()
    if exists:
        new_slug = "{} {}".format(slug, querystring.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)    

   

