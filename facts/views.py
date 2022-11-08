
from django.http import HttpResponseRedirect
from django.shortcuts import render

from facts.forms import FactForm
from facts.models import Fact

# Create your views here.


def home(request):
    current_fact = Fact.objects.raw(
        'select * from facts_fact order by rand() limit 1')[0]
    context = {
        "current_fact": current_fact
    }
    return render(request, 'facts/index.html', context=context)


def new_fact(request):
    if request.method == 'POST':
        form = FactForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FactForm()

    return render(request, 'facts/form.html', {'form': form})
