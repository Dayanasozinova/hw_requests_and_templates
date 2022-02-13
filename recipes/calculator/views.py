from django.shortcuts import render


def omlet(request):
    servings = int(request.GET.get('servings'))
    context = {
        'recipe': {
            'omlet': {
                'яйца, шт': 2 * servings,
                'молоко, л': 0.1 * servings,
                'соль, ч.л.': 0.5 * servings,
            },
        }
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    servings = int(request.GET.get('servings'))
    context = {
        'recipe': {
            'buter': {
                'хлеб, ломтик': 1 * servings,
                'колбаса, ломтик': 1 * servings,
                'сыр, ломтик': 1 * servings,
                'помидор, ломтик': 1 * servings,
            },
        }
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = int(request.GET.get('servings'))
    context = {
        'recipe': {
            'pasta': {
                'макароны, г': 0.3 * servings,
                'сыр, г': 0.05 * servings,
            },
        }
    }

    return render(request, 'calculator/index.html', context)
