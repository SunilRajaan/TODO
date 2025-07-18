from django.contrib import admin
from django.urls import path
from base.views import home, create_todo, edit_todo, delete_todo, create_description_with_ai


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('create/todo/', create_todo, name='create_todo'),
    path('edit/todo/<int:pk>', edit_todo, name='edit_todo'),
    path('delete/todo/<int:pk>', delete_todo, name='delete_todo'),
]
