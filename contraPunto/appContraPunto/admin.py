from django.contrib import admin

# Register your models here.

from .models import (Categoria, Medio, Noticia, Comparativa,SesgoEmocional, SesgoIdeologico, SesgoEnfoque, EncuestaFlash, RespuestaFlash)

admin.site.register(Categoria)
admin.site.register(Medio)
admin.site.register(Noticia)
admin.site.register(Comparativa)
admin.site.register(SesgoEmocional)
admin.site.register(SesgoIdeologico)
admin.site.register(SesgoEnfoque)
admin.site.register(EncuestaFlash)
admin.site.register(RespuestaFlash)