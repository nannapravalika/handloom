from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import add_weaver, list_weavers, remove_weaver, edit_weaver
from . import views

urlpatterns = [
    path('add_weaver/', views.add_weaver, name='add_weaver'),
    path('list_weavers/', views.list_weavers, name='list_weavers'),
    path('edit_weaver/<int:id>/', views.edit_weaver, name='edit_weaver'),
    path('remove_weaver/<int:id>/', views.remove_weaver, name='remove_weaver'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)