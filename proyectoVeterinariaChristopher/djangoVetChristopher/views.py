from django.shortcuts import render
from djangoVetChristopher.models import Mascotas, Tratamientos
from . import forms
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    data = {
        'nombre':'Animaliacos',
        'profesion':'Clinica veterinaria',
        'presentacion':'La Clínica Veterinaria Animaliacos es un refugio de salud, bienestar y amor para las mascotas. Nuestra pasión y compromiso por el cuidado de los animales es evidente en cada aspecto de nuestra clínica. Aquí, nos dedicamos a ofrecer una atención veterinaria excepcional, combinando la experiencia de profesionales altamente capacitados con un ambiente amigable y compasivo para las mascotas y sus dueños',
        'imagen1':'https://estaticos-cdn.prensaiberica.es/clip/c7cf76a0-d2ee-4937-87d5-fc57f2f7d35f_16-9-discover-aspect-ratio_default_0.jpg',
        'name':'Christopher Campos',
        'direc':'Aveida San Miguel 31 ote.'
}   
    return render(request, 'djangoVetChristopher/index.html', data)


def viewTratamientos(request):
    tratamientps = Tratamientos.objects.all()
    data = {'tratamientos': tratamientps}
    return render(request, 'djangoVetChristopher/viewTratamientos.html', data)

def viewMascotas(request):
    mascotas = Mascotas.objects.all()
    data = {'mascotas': mascotas}
    return render(request, 'djangoVetChristopher/viewMascotas.html', data)


def addTratamiento(request):

    form = forms.Tratamiento()

    if request.method == 'POST':
        form = forms.Tratamiento(request.POST)
        if form.is_valid():
            print("Formulario valido")
            form.save()
            return HttpResponseRedirect(reverse('lista_tratamientos'))

    data = {'form': form,
            'titulo':'Editar Tratamiento'
            }
    return render(request, 'djangoVetChristopher/formTratamiento.html',data)


def deleteTratamiento(request, id):
    tratamiento = Tratamientos.objects.get(id = id)
    tratamiento.delete()
    return HttpResponseRedirect(reverse('lista_tratamientos'))

def editTratamiento(request, id):

    tratamiento = Tratamientos.objects.get(id=id)

    form = forms.Tratamiento(instance=tratamiento)
    if request.method == 'POST':
        form = forms.Tratamiento(request.POST, instance=tratamiento)
        if form.is_valid():
            print("Formulario valido")
            form.save()
            return HttpResponseRedirect(reverse('lista_tratamientos'))
        else:
            print("Errores: ",form.errors)

    data = {'form': form,
            'titulo':'Editar Tratamiento'
            }
    return render(request, 'djangoVetChristopher/formTratamiento.html',data)

def addMascota(request):

    form = forms.Mascota()

    if request.method == 'POST':
        form = forms.Mascota(request.POST)
        if form.is_valid():
            print("Formulario valido")
            form.save()
            return HttpResponseRedirect(reverse('lista_mascotas'))

    data = {'form': form,
            'titulo':'Agregar Mascota'
            }
    return render(request, 'djangoVetChristopher/formMascota.html',data)


def deleteMascota(request, id):
    """ Buscar la mascota correspondiente con su id """
    mascota = Mascotas.objects.get(id = id)
    mascota.delete()
    return HttpResponseRedirect(reverse('lista_mascotas'))


def editMascota(request, id):
    """ Buscamos la mascota a editar """
    mascota = Mascotas.objects.get(id=id)
    """ Generar formulario con datos de la mascota """
    form = forms.Mascota(instance=mascota)
    if request.method == 'POST':
        form = forms.Mascota(request.POST, instance=mascota)
        if form.is_valid():
            print("Formulario valido")
            form.save()
            return HttpResponseRedirect(reverse('lista_mascotas'))
        else:
            print("Errores: ",form.errors)

    data = {'form': form,
            'titulo':'Editar Mascota'
            }
    return render(request, 'djangoVetChristopher/formMascota.html',data)
