"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import home, todo_types, create_todo, edit_todo, delete_todo, create_todo_types, edit_todo_types, delete_todo_types


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('create/todo/', create_todo, name='create_todo'),
    path('edit/todo/<int:pk>', edit_todo, name='edit_todo'),
    path('delete/todo/<int:pk>', delete_todo, name='delete_todo'),
    # Todos TYPES 
    path("todo_types/", todo_types, name='todo_types'),
    path('create/types', create_todo_types, name='create_types'),
    path('edit/types/<int:pk>/', edit_todo_types, name='edit_types'),
    path('delete/types/<int:pk>/', delete_todo_types, name='delete_types'),
]
