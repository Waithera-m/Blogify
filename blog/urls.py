from django.urls import path
from blog import views

urlpatterns = [
    path('', views.posts_home, name='posts_home'),
    path('create/', views.create_post, name='create'),
    path('update/', views.update_post, name='update'),
    path('delete/', views.delete_post, name='delete'),
    path('post/<int:pk>', views.get_single_post, name='single_post'),
]