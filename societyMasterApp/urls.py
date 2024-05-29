from django.urls import path
from .views import list_society, create_society, edit_society, delete_society

urlpatterns = [
    path('list-society/', list_society, name='list_society'),
    path('create-society/', create_society, name='create_society'),
    path('edit_society/<int:id>/', edit_society, name='edit_society'),
    path('delete_society/<int:id>/', delete_society, name='delete_society'),
]
