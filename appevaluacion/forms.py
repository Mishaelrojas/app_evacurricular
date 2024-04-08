from django import forms 
from django.forms import fields 
from appevaluacion.models import *
from django.contrib.auth.models import User
import datetime

class PostulanteForm(forms.ModelForm):
    class Meta:
        model = Postulante
        fields = [
            'idPostulante',
            'codigo',
            'ap_paterno',            
            'ap_materno',
            'nombres',
            'dni',
            'email',
            'celular',            
            'pdf_curriculum',            
            'doctorado',            
            'maestria',
            'unidad',
            'modalidad',
        ]
        widgets = {              
            'pdf_curriculum': forms.TextInput(attrs={'readonly': True}),                   
        }

class EvaluacionForm(forms.ModelForm):
    def __init__(self, *args, unidades=None, **kwargs):
        super().__init__(*args, **kwargs)
        postulantes_asignados = Evaluacion.objects.values_list('postulante', flat=True)
        self.fields['postulante'].queryset = Postulante.objects.exclude(idPostulante__in=postulantes_asignados)
      
    class Meta:
        model = Evaluacion        
        fields = [
            'idEvaluacion',
            'codigo_evaluacion',
            'estado_evaluacion',          
            'postulante',         
            'evaluador',
            'fecha_creacion',          
        ]
        exclude = ['codigo_evaluacion']
        widgets = {              
            'codigo_evaluacion': forms.TextInput(attrs={'required': False, 'readonly': True}),
            'fecha_creacion': forms.TextInput(attrs={'readonly': True}),       
        }
        labels = {
            'fecha_creacion': '',
        }


class DetalleEvaluacionForm(forms.ModelForm):
 

    class Meta:
        model = DetalleEvaluacion
        fields =  [
            'idDetalleEva',
            'evaluacion',           
            'puntaje_promedioP',
            'puntaje_cursosEva',
            'puntaje_partCientifica',
            'puntaje_docenciaUni',
            'puntaje_idiomaExt',
            'puntaje_capacitacion',
            'puntaje_libroInscritos',
            'puntaje_publicaciones',
            'puntaje_proyInvestig',
            'puntaje_asesoriaProy',
            'puntaje_produccionCien',
            'puntajeFinal',       
        ]
        labels = {
            'puntaje_promedioP': '',
            'puntaje_cursosEva': '',
            'puntaje_partCientifica': '',
            'puntaje_docenciaUni': '',
            'puntaje_idiomaExt': '',
            'puntaje_capacitacion': '',
            'puntaje_libroInscritos': '',
            'puntaje_publicaciones': '',
            'puntaje_proyInvestig': '',
            'puntaje_asesoriaProy': '',
            'puntaje_produccionCien': '',
            'puntajeFinal': '',    
            
            # Define las etiquetas personalizadas para otros campos aquí
        }
        widgets = {
            'evaluacion': forms.TextInput(attrs={'required': False, 'readonly': True}),
            'puntaje_capacitacion': forms.TextInput(attrs={'required': False, 'readonly': True}),
            'puntaje_produccionCien': forms.TextInput(attrs={'required': False, 'readonly': True}),
            'puntajeFinal': forms.TextInput(attrs={'required': False, 'readonly': True})
        }

