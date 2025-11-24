from django.db.models import Count

def calcular_dominancia_enfoque(noticias_queryset):
    total = noticias_queryset.count()
    if total == 0:
        return 0

    # Agrupa por enfoque y cuenta cuántas noticias hay de cada uno
    conteos = noticias_queryset.values("sesgo_enfoque").annotate(total=Count("id"))

    # Encuentra el mayor número de noticias en un enfoque
    maximo = max(item["total"] for item in conteos)

    # Escala a rango 0–5
    dominancia = (maximo / total) * 5

    return round(dominancia, 2)
