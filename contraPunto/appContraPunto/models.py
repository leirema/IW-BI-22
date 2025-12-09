# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

# Modelos para los sesgos
class SesgoIdeologico(models.Model):
    nombre = models.CharField(max_length=50)
    rango_min = models.FloatField()
    rango_max = models.FloatField()
    color = models.CharField(max_length=20, default="#999999")
    def __str__(self):
        return self.nombre

class SesgoEmocional(models.Model):
    nombre = models.CharField(max_length=50)
    rango_min = models.FloatField()
    rango_max = models.FloatField()
    def __str__(self):
        return self.nombre

class SesgoEnfoque(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre


#Modelos principales
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Image')
    color = models.CharField(max_length=20, default="#cccccc")
    def __str__(self):
        return self.nombre

class Medio(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[
        ('periodico', 'Periodico'),
        ('podcast', 'Podcast'),
        ('television', 'Television'),
        ('radio', 'Radio'),
        ('revista', 'Revista'),
    ])
    pais = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Image')
    web = models.URLField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Comparativa(models.Model):
    titulo = models.CharField(max_length=200)
    claves = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    categoria = models.ManyToManyField(Categoria)
    contenido = models.TextField()
    objetividad = models.FloatField(null=True, blank=True)
    imagen = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Image')
    destacada = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.titulo} ({self.fecha})"

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    fecha = models.DateField()
    medio = models.ForeignKey(Medio, on_delete=models.CASCADE)
    enlace = models.URLField(max_length=200)
    imagen = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Image')
    sesgo_ideologico = models.FloatField(null=True, blank=True)  # -5=progresista, 0=centro, 5=conservador
    sesgo_emocional = models.FloatField()    # 0=analítico, 5=sensacionalista
    sesgo_enfoque = models.ForeignKey(SesgoEnfoque, on_delete=models.CASCADE )
    comparativa = models.ForeignKey(Comparativa, on_delete=models.CASCADE, related_name="noticias")
    
    def get_sesgo_ideologico(self):
        from django.db.models import Q
        intervalo = SesgoIdeologico.objects.filter(
            Q(rango_min__lte=self.sesgo_ideologico) & Q(rango_max__gte=self.sesgo_ideologico)).first()
        return intervalo.nombre if intervalo else "Sin evaluar"
    
    def get_sesgo_emocional(self):
        from django.db.models import Q
        intervalo = SesgoEmocional.objects.filter(
            Q(rango_min__lte=self.sesgo_emocional) & Q(rango_max__gte=self.sesgo_emocional)).first()
        return intervalo.nombre if intervalo else "Sin evaluar"

    def __str__(self):
        return f"{self.titulo} - {self.medio.nombre} ({self.fecha})"

# FORMULARIO CLASES NUEVAS
class EncuestaFlash(models.Model):
    pregunta_actualidad = models.CharField(max_length=300)
    opciones_actualidad = models.JSONField()  # [{'codigo':'a','texto':'...'}, ...]
    respuesta_correcta = models.CharField(max_length=1)  # 'a','b','c','d'
    posturas = models.JSONField() # [{'codigo':'A','texto':'...'}, ...]
    fecha_publicacion = models.DateField()
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"Encuesta {self.fecha_publicacion}"

class RespuestaFlash(models.Model):
    #encuesta actualidad
    encuesta = models.ForeignKey(EncuestaFlash, on_delete=models.CASCADE)
    respuesta_actualidad = models.CharField(max_length=1)
    es_correcta = models.BooleanField()  
    respuesta_postura = models.CharField(max_length=1)
    #coleción de datos
    sesgo_visibilidad = models.IntegerField()
    tipo_info_valiosa = models.CharField(max_length=20)
    resumen_usuario = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Formulario {self.timestamp}"
 



