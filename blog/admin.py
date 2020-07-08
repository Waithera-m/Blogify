from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    """
    class customizes admin page
    """
    list_display = ['title', 'time_stamp', 'updated']
    list_filter = ['time_stamp', 'updated']
    search_fields = ['title', 'content']
    list_editable = ['title']
    list_display_links = ['time_stamp']
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)