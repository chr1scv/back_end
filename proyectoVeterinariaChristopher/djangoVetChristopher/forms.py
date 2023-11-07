from django import forms
from djangoVetChristopher.models import Mascotas, Tratamientos
from django.core import validators

class Mascota(forms.Form):

    nombre = forms.CharField(
        validators=[validators.MinLengthValidator(5),
            validators.MaxLengthValidator(20)]
    )
    microchip = forms.IntegerField()
    fecha_de_atencion = forms.DateField()
    motivo = forms.CharField(max_length=30)
    diagnostico = forms.CharField(max_length=30)
    tratamiento = forms.ModelChoiceField(queryset=Tratamientos.objects.all())
    observaciones = forms.CharField(max_length=30)
    valor = forms.IntegerField()

    nombre.widget.attrs['class'] = 'form-control'
    microchip.widget.attrs['class'] = 'form-control'
    fecha_de_atencion.widget.attrs['class'] = 'form-control'
    motivo.widget.attrs['class'] = 'form-control'
    diagnostico.widget.attrs['class'] = 'form-control'
    tratamiento.widget.attrs['class'] = 'form-control'
    observaciones.widget.attrs['class'] = 'form-control'
    valor.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Mascotas
        fields = '__all__'


class Mascota(forms.ModelForm):

    nombre = forms.CharField(
        validators=[validators.MinLengthValidator(5),
            validators.MaxLengthValidator(20)]
    )
    microchip = forms.IntegerField()
    fecha_de_atencion = forms.DateField()
    motivo = forms.CharField(max_length=30)
    diagnostico = forms.CharField(max_length=30)
    tratamiento = forms.ModelChoiceField(queryset=Tratamientos.objects.all())
    observaciones = forms.CharField(max_length=30)
    valor = forms.IntegerField()


    nombre.widget.attrs['class'] = 'form-control'
    microchip.widget.attrs['class'] = 'form-control'
    fecha_de_atencion.widget.attrs['class'] = 'form-control'
    motivo.widget.attrs['class'] = 'form-control'
    diagnostico.widget.attrs['class'] = 'form-control'
    tratamiento.widget.attrs['class'] = 'form-control'
    observaciones.widget.attrs['class'] = 'form-control'
    valor.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Mascotas
        fields = '__all__'


class Tratamiento(forms.Form):


    nombre = forms.CharField(
        validators=[validators.MinLengthValidator(5),
            validators.MaxLengthValidator(20)]
    )


    nombre.widget.attrs['class'] = 'form-control'
    
class Tratamiento(forms.ModelForm):


    nombre = forms.CharField(
        validators=[validators.MinLengthValidator(5),
                    validators.MaxLengthValidator(20)]
    )
        
    nombre.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Tratamientos
        fields = '__all__'
