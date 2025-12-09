from django import forms


class RespuestaFlashForm(forms.Form):
    respuesta_actualidad = forms.CharField(widget=forms.HiddenInput())
    respuesta_postura = forms.CharField(widget=forms.HiddenInput())
    sesgo_visibilidad = forms.IntegerField(min_value=0, max_value=10)
    tipo_info_valiosa = forms.ChoiceField(choices=[
        ('datos', 'Datos verificables'),
        ('contexto', 'Contexto historico'),
        ('testimonios', 'Testimonios personales'),
        ('opinion', 'Opinion argumentada'),
    ])
    resumen_usuario = forms.CharField(
        widget=forms.Textarea, 
        required=False
    )