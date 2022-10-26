import random

from django.shortcuts import render

facts = ["Hay 1424 cosas en una habitación promedio con las que Chuck Norris podría matarte. Incluyendo la habitación en sí.",
         "Chuck Norris es la medida del sistema internacional del dolor.",
         "Chuck Norris ganó un concurso sobre permanecer debajo del agua y ganó. Cabe destacar que su contrincante era pez.",
         "Las lágrimas de Chuck Norris curan el cáncer. Lástima que jamás haya llorado.",
         "Chuck Norris dona sangre a menudo. Pero rara vez es la suya.",
         "La gente usa pijamas de Superman. Superman usa pijamas de Chuck Norris."]

# Create your views here.


def home(request):
    current_fact = random.choice(facts)
    context = {
        "current_fact": current_fact
    }
    return render(request, 'facts/index.html', context=context)
