from django.shortcuts import render
from anevolina.models import Project

# Create your views here.

def index(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'anevolina/index.html', context)


def project_details(request, pk):
    switcher = {
        1: words_game,
        2: converter
    }

    func = switcher.get(pk, lambda: index)
    return func(request)

def words_game(request):

    return render(request, 'anevolina/words_game.html', {})

def converter(request):

    return render(request, 'anevolina/converter.html', {})

