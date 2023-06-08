from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('abrir/', views.abrirGuardar, name='abrir'),
    path('guardar/', views.guardar, name='guardar'),
    path('borrar/<int:id>/', views.borrar, name='borrar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('pelicula/<int:id>/', views.pelicula, name='pelicula'),
]