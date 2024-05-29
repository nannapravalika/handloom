from django.urls import path
from .views import add_master_weaver, list_master_weaver, delete_master_weaver, edit_master_weaver

urlpatterns = [
    path('add-master-weaver/', add_master_weaver, name='add_master_weaver'),
    path('list-master-weaver/', list_master_weaver, name='list_master_weaver'),
    path('edit-master-weaver/<int:id>/', edit_master_weaver, name='edit_master_weaver'),
    path('delete-master-weaver/<int:id>/', delete_master_weaver, name='delete_master_weaver'),

]