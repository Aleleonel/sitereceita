from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Receitas"""

    receitas = {
        1: 'Lazanha',
        2: 'Caldo Verde de Ervilha',
        3: 'Caldo de Feijão',
        4: 'Vinho Quente',
        5: 'Cocada Caseira',
        6: 'Pipoca com Chocolate',
        7: 'Bolo de Cenoura'
    }

    context = {
        'nome_da_receita': receitas
    }

    return render(request, 'index.html', context)


def receita(request):
    """Paginas de receitas"""

    return render(request, 'receita.html')
