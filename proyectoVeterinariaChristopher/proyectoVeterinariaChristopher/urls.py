from django.contrib import admin
from django.urls import path
from djangoVetChristopher.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="indexes"),
    path('mascotas/', viewMascotas, name='lista_mascotas'),
    path('tratamientos/', viewTratamientos, name='lista_tratamientos'),
    path('addMascota/', addMascota, name='agregarMascota'),
    path('deleteMascota/<int:id>', deleteMascota, name='eliminarMascota'),
    path('editMascota/<int:id>', editMascota, name='editarMascota'),
    path('editTratamiento/<int:id>', editTratamiento, name='editarTratamiento'),
    path('addTratamiento/', addTratamiento, name='agregarTratamiento'),
    path('deleteTratamiento/<int:id>', deleteTratamiento, name='borrarTratamiento'),
]