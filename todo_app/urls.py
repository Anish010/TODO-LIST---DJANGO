from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.index, name="index"),
    path('add', views.addNewToDo, name="add"),
    path('complete/<todo_id>', views.completeToDo, name="complete"),
    path('delete', views.deleteToDo, name="delete"),
    path('delete_all', views.deleteAll, name="delete_all")
]
