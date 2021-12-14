from django.shortcuts import render
from pathlib import Path
import os
import numpy as np

# Create your views here.

def index(request):
    return render(request, "index.html")

def games(request):

    BASE_DIR = Path(__file__).resolve().parent.parent
    games_paths = os.path.join(BASE_DIR,'static/Proyectos_yo_programo.txt')

    with open(games_paths, 'r') as file:
        data = file.read().replace('\n\n', ': ')

    data = data.split(": ")

    links = [
    'https://scratch.mit.edu/projects/605379639/',
    'https://scratch.mit.edu/projects/604253418/',
    'https://scratch.mit.edu/projects/605454832/',
    'https://scratch.mit.edu/projects/606594268/',
    'https://scratch.mit.edu/projects/603010140/',
    'https://scratch.mit.edu/projects/599155722/',
    'https://scratch.mit.edu/projects/545298562/',
    'https://scratch.mit.edu/projects/603006124/',
    'https://scratch.mit.edu/projects/539669007/',
    'https://scratch.mit.edu/projects/604268767/',
    'https://scratch.mit.edu/projects/607610887/',
    'https://scratch.mit.edu/projects/606605328/',
    ]

    links = np.array(links)
    context = {
       'links' : np.random.choice(links, size=9, replace=False),
    }

    print(links)

    return render(request, "games.html", context=context)