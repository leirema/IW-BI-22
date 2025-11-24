from django.db.models import Count, Q
from .models import SesgoEnfoque

def calcular_dominancia_enfoque(noticias_queryset):
    total = noticias_queryset.count()
    if total == 0:
        return 0, 'N/A'

    # Agrupa por enfoque y cuenta cuántas noticias hay de cada uno
    conteos = noticias_queryset.values("sesgo_enfoque").annotate(total=Count("id"))

    # Encuentra el mayor número de noticias en un enfoque
    ganador = max(conteos, key=lambda x: x["total"])
    maximo = ganador["total"]

    # Escala a rango 0–5
    dominancia = (maximo / total) * 5

    return round(dominancia, 2), SesgoEnfoque.objects.get(id=ganador["sesgo_enfoque"]).nombre

def calcular_categorias_cubiertas(comparativas_queryset, categorias_queryset):
    conteos = (
        categorias_queryset
        .annotate( # Agrega una columna de conteo num de cuantas comparativas están asociadas a cada categoría
            num=Count(  
                'comparativa',
                filter=Q(comparativa__in=comparativas_queryset), # Solo cuenta si la comparativa está en el queryset dado
                distinct=True
            )
        )
        .order_by('nombre')
        
    )
    # Devuele tres variables en vez de el objeto entero de categorias
    labels = [cat.nombre for cat in conteos]
    data = [cat.num for cat in conteos]
    colors = [cat.color for cat in conteos]
    return labels, data, colors