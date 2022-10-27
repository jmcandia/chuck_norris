from django.shortcuts import render

from facts.models import Fact

# Create your views here.


def home(request):
    current_fact = Fact.objects.raw(
        'select * from facts_fact order by rand() limit 1')[0]
    context = {
        "current_fact": current_fact
    }
    return render(request, 'facts/index.html', context=context)
