from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_create_posts),
    path('posts/<int:id>', views.get_delete_post),
]
