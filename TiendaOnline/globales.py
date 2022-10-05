from Categorias.models import Category

def data_templates(request):
    return {
        "categorias": Category.objects.all(),
    }