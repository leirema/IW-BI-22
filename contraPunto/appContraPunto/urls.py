# -*- coding: utf-8 -*-
from django.urls import path
from .views import (ComparativaListView, HomeView, ComparativaDetailView, CategoriaDetailView,
                    CategoriaListView, MedioDetailView, MedioListView, 
                    NoticiaDetailView, RespuestaFlashFormView, ResultadoFlashView)
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('comparativa/<int:pk>/', ComparativaDetailView.as_view(), name='comparativa'),
    path('comparativas/', ComparativaListView.as_view(), name='comparativas'),
    path('categoria/<int:pk>/', CategoriaDetailView.as_view(), name='categoria'),
    path('categorias/', CategoriaListView.as_view(), name='categorias'),
    path('medio/<int:pk>/', MedioDetailView.as_view(), name='medio'),
    path('medios/', MedioListView.as_view(), name='medios'),
    path('noticia/<int:pk>/', NoticiaDetailView.as_view(), name='noticia'),
    path('flash/', RespuestaFlashFormView.as_view(), name='encuesta_flash'),
    path('flash/resultado/', ResultadoFlashView.as_view(), name='resultado_flash'),
]