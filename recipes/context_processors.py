from .models import Category

def categories_processor(request):
    """
    Context processor to make categories available to all templates,
    specifically for the Recipe Index dropdown in the navbar.
    """
    return {
        'default_categories': Category.objects.all().order_by('name')
    }
