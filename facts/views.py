
from django.http import HttpResponseRedirect
from django.shortcuts import render

from facts.forms import FactForm, LoginForm
from facts.models import Fact

# Create your views here.


def home(request):
    # Verificar que no exista la sesión
    if not request.session.has_key('username'):
        # Si la sesión no existe, entonces me lleva al login
        return HttpResponseRedirect('/login')

    username = request.session['username']

    current_fact = Fact.objects.raw(
        'select * from facts_fact order by rand() limit 1')[0]
    context = {
        "current_fact": current_fact,
        "username": username
    }
    return render(request, 'facts/index.html', context=context)


def new_fact(request):
    # Verificar que no exista la sesión
    if not request.session.has_key('username'):
        # Si la sesión no existe, entonces me lleva al login
        return HttpResponseRedirect('/login')

    username = request.session['username']

    if request.method == 'POST':
        form = FactForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FactForm()

    return render(request, 'facts/form.html', {'form': form, 'username': username})


def login(request):
    # Verificar que no exista la sesión
    if request.session.has_key('username'):
        # Si la sesión existe, entonces me lleva al home
        return HttpResponseRedirect('/')
    else:
        # Si la sesión no existe, verifica el formulario
        if request.method == 'POST':
            # Si se recibe el formulario
            form = LoginForm(request.POST)
            if form.is_valid():
                # Si el formulario es válido, se verifican los datos
                username = form.cleaned_data['email']
                password = form.cleaned_data['password']
                if username == 'admin@inacap.cl' and password == '12345678':
                    # Si los datos son válidos, crea la sesión
                    request.session['username'] = username
                    return HttpResponseRedirect('/')
        else:
            # Si no estamos recibiendo el formulario, entonces envíamos uno vacío
            form = LoginForm()

    return render(request, 'facts/login.html', {'form': form})


def logout(request):
    if request.session.has_key('username'):
        del request.session['username']

    return HttpResponseRedirect('login/')
