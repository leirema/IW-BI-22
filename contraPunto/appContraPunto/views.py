# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Noticia, Categoria, Comparativa, Medio
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
        context['noticias_relacionadas'] = (
            Noticia.objects.filter(medio = self.object)
            .order_by('sesgo_ideologico')
            )
        # Agregar comparativas atravesadas por la relación noticias del medio
        context['comparativas_atravesadas'] = (
            Comparativa.objects.filter(noticias__medio= self.object)
            .order_by('-fecha')
            )
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

class NoticiaListView(ListView):
    model = Noticia
    template_name = 'noticia_list.html'
    queryset = Noticia.objects.order_by('-fecha')
    context_object_name = 'noticias'