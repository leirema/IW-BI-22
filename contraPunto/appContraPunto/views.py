# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import DetailView, ListView, FormView, TemplateView
from .models import Noticia, Categoria, Comparativa, Medio, EncuestaFlash, RespuestaFlash
from .forms import RespuestaFlashForm
from .utils import calcular_dominancia_enfoque, calcular_categorias_cubiertas
from django.db.models import Avg, Count
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class HomeView(ListView):
    model = Comparativa
    template_name = 'home.html'
    context_object_name = 'comparativas_destacadas'
    def get_queryset(self):
        # Lógica para obtener la lista de categorías para la página de inicio
        return Comparativa.objects.filter(destacada=True).order_by('-fecha')[:5] # Las 5 más recientes

class ComparativaDetailView(DetailView):
    model = Comparativa
    template_name = 'comparativa_detail.html'
    context_object_name = 'comparativa'
    def get_context_data(self, **kwargs):
        context = super(ComparativaDetailView, self).get_context_data(**kwargs)
        # Agregar noticias relacionadas a la comparativa en el contexto
        context['noticias_relacionadas'] = (
            Noticia.objects.filter(comparativa = self.object)
            .order_by('sesgo_ideologico')
            )
        return context

class ComparativaListView(ListView):
    model = Comparativa
    template_name = 'comparativa_list.html'
    queryset = Comparativa.objects.order_by('-fecha')
    context_object_name = 'comparativas'

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria_detail.html'
    context_object_name = 'categoria'
    def get_context_data(self, **kwargs):
        context = super(CategoriaDetailView, self).get_context_data(**kwargs)
        # Agregar comparativas relacionadas a la categoría en el contexto
        context['comparativas_relacionadas'] = (
            Comparativa.objects.filter(categoria = self.object)
            .order_by('-fecha')
            )
        return context

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    queryset = Categoria.objects.all()
    context_object_name = 'categorias'

class MedioDetailView(DetailView):
    model = Medio
    template_name = 'medio_detail.html'
    context_object_name = 'medio'
    def get_context_data(self, **kwargs):
        context = super(MedioDetailView, self).get_context_data(**kwargs)
        # Agregar noticias relacionadas al medio en el contexto
        noticias_relacionadas = Noticia.objects.filter(medio = self.object)
        context['noticias_relacionadas'] = noticias_relacionadas.order_by('sesgo_ideologico')
        # Calcular datos de las gráficas de sesgo ideológico
        ideologia_real = noticias_relacionadas.aggregate(Avg("sesgo_ideologico"))["sesgo_ideologico__avg"]
        if(ideologia_real < 0):
            texto_ideologia = "Progresista"
        else:
            texto_ideologia = "Conservador"
        
        if ideologia_real is not None:
            ideologia_abs = abs(ideologia_real)
        else:
            ideologia_abs = 0
        
        context['label_ideologia'] = texto_ideologia
        data_emocion = noticias_relacionadas.aggregate(Avg("sesgo_emocional"))["sesgo_emocional__avg"]
        data_enfoque, context['label_enfoque'] = calcular_dominancia_enfoque(noticias_relacionadas)
        context['data_sesgo'] = {
            "ideologia": ideologia_abs,
            "emocion": data_emocion,
            "enfoque": data_enfoque,
        }
        context['obj_media'] = round(5-(ideologia_abs + data_emocion + data_enfoque)/3, 2)
        # Agregar comparativas atravesadas por la relación noticias del medio
        comparativas_atravesadas = Comparativa.objects.filter(noticias__medio= self.object).distinct()
        context['comparativas_atravesadas'] = comparativas_atravesadas.order_by('-fecha')      
        #Clacular datos para la gráfica de panorama de categrías cubiertas
        context['label_categorias'], context['data_categorias'], context['color_categorias'] = calcular_categorias_cubiertas(comparativas_atravesadas, Categoria.objects.all())
        return context

class MedioListView(ListView):
    model = Medio
    template_name = 'medio_list.html'
    queryset = Medio.objects.order_by('nombre')
    context_object_name = 'medios'

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticia_detail.html'
    context_object_name = 'noticia'

class ResultadoFlashView(TemplateView):
    template_name = "flash_resultado.html"
    def get(self, request, *args, **kwargs):
        resp_id = request.GET.get("id")
        if not resp_id:
            return HttpResponseRedirect(reverse("encuesta_flash"))
        self.respuesta = RespuestaFlash.objects.get(id=resp_id)
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resp_id = self.request.GET.get("id")
        respuesta = RespuestaFlash.objects.get(id=resp_id)
        context["respuesta"] = respuesta
        #gráfica AB
        conteo = (
            RespuestaFlash.objects
            .filter(encuesta=respuesta.encuesta)
            .values('respuesta_postura')
            .annotate(total=Count('id'))
        )
        context["label_postura"] = [item['respuesta_postura'] for item in conteo]
        context["data_postura"] = [item['total'] for item in conteo]
        return context

class RespuestaFlashFormView(FormView):
    form_class = RespuestaFlashForm
    template_name = 'flash_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Encuesta activa del día
        context['encuesta'] = EncuestaFlash.objects.filter(activa=True).latest('fecha_publicacion')
        return context

    def form_valid(self, form):
        encuesta = EncuestaFlash.objects.filter(activa=True).latest('fecha_publicacion')
        cd = form.cleaned_data
        #Guardar respuesta
        respuesta = RespuestaFlash.objects.create(
            encuesta=encuesta,
            respuesta_actualidad=cd['respuesta_actualidad'],
            es_correcta=(cd['respuesta_actualidad'] == encuesta.respuesta_correcta),
            respuesta_postura=cd['respuesta_postura'],
            sesgo_visibilidad=cd['sesgo_visibilidad'],
            tipo_info_valiosa=cd['tipo_info_valiosa'],
            resumen_usuario=cd['resumen_usuario'],
        )
        return HttpResponseRedirect(
            reverse('resultado_flash') + f'?id={respuesta.id}'
        )
    
