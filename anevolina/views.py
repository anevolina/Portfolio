from googletrans import Translator
import logging

from django.shortcuts import render
from anevolina.models import Project
from portfolio.settings import STATICFILES_DIRS
from . import forms

# Import my modules
from anevolina.modules.converter import ARConverter


# Create your views here.

def index(request, project=None):
    if project:
        logging.basicConfig(filename='odd_projects.log', level=logging.INFO)
        logging.INFO('Project without a view was detected: {}-{}'.format(project.pk, project.title))

    projects = Project.objects.all()

    context = {'projects': projects}

    return render(request, 'anevolina/index.html', context)


def project_details(request, pk):
    project = Project.objects.get(pk=pk)

    switcher = {
        1: blog,
        2: words_game,
        3: converter
    }

    func = switcher.get(pk, lambda: index)
    return func(request, project)

def words_game(request, project):

    context = {'project': project}
    return render(request, 'anevolina/words_game.html', context)

def converter(request, project):
    conv_recipe = 'converted text\'s here'
    English = True


    if request.method != 'POST':
        form = forms.ConverterForm()

    else:
        form = forms.ConverterForm(request.POST)

        if form.is_valid():

            converter = ARConverter()
            text = form.cleaned_data['recipe']
            conv_recipe = ''
            for line in text.split('\n'):
                conv_recipe += converter.process_line(line) + '\n'

            to_translate = request.POST.get('to_translate')
            if to_translate == 'RU':
                English = False
                translator = Translator(service_urls=[
                    'translate.google.com',
                    'translate.google.co.kr', ])
                translation = translator.translate(conv_recipe, dest='ru')
                conv_recipe = translation.text

    context = {'form': form, 'translation': conv_recipe, 'En': English, 'project': project}

    return render(request, 'anevolina/converter.html', context)

def blog(request, project):


    context = {'project': project}
    return render(request, 'anevolina/this_blog.html', context)