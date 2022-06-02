from django.urls import path
from .views import post_list, post_create,post_update,post_delete,post_details


urlpatterns = [
    path('', post_list, name='home'),
    path('create/', post_create, name='create'),
    path('update/<int:id>', post_update, name='update'),
    path('delete/<int:id>', post_delete, name='delete'),
    path('details/<int:id>', post_details, name='details'),
]
