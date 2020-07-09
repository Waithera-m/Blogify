from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.posts_home, name='posts_home'),
    path('create/', views.create_post, name='create'),
    path('update/<int:pk>', views.update_post, name='update'),
    path('delete/<int:pk>', views.delete_post, name='delete'),
    path('<int:pk>/', views.DetailView.as_view(), name='details'),
]