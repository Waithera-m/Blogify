from django.urls import path
from blog import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    path('', views.posts_home, name='posts_home'),
    path('create/', views.create_post, name='create'),
    path('update/<int:pk>', views.update_post, name='update'),
    path('delete/<int:pk>', views.delete_post, name='delete'),
    path('<slug>/', views.post_detail, name='details'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)