from django import forms
from .models import Activo, Report


class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activo
        fields = ['titulo', 'proyecto', 'fecha_inicio',
                  'fecha_fin', 'estado_activo', 'ordenar_por']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['proyecto'].required = False
        self.fields['estado_activo'].required = False
        self.fields['ordenar_por'].required = False


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['nombre_responsable', 'email',
                  'estado_activo', 'descripcion', 'activo_titulo']
