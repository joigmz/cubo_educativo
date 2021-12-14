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
    links, nombres = [], []

    for i in range(len(data)):
        if i%2 != 0:
            links.append(data[i])
        else:
            nombres.append(data[i])

    links, nombres = np.array(links), np.array(nombres)

    context = {
       'links' : links[:5],
       'nombres': nombres[:5]
    }

    return render(request, "games.html", context=context)