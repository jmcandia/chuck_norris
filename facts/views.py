
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from facts.forms import FactForm, LoginForm
from facts.models import Fact

from .serializers import FactSerializer

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
                # Usa la función authenticate de django.contrib.auth
                user = authenticate(username=username, password=password)
                if user is not None:
                    # Si los datos son válidos, crea la sesión
                    request.session['username'] = user.first_name or user.username
                    return HttpResponseRedirect('/')
        else:
            # Si no estamos recibiendo el formulario, entonces envíamos uno vacío
            form = LoginForm()

    return render(request, 'facts/login.html', {'form': form})


def logout(request):
    if request.session.has_key('username'):
        del request.session['username']

    return HttpResponseRedirect('/login')


@api_view(['GET', 'POST'])
def facts_list(request):
    # Devuelve todos los datos
    if request.method == 'GET':
        facts = Fact.objects.all()
        serializer = FactSerializer(facts, many=True)
        return Response(serializer.data)

    # Crea un nuevo registro
    if request.method == 'POST':
        serializer = FactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def fact_detail(request, id):
    # Verifica si existe el recurso
    try:
        fact = Fact.objects.get(id=id)
    except Fact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Obtiene un recurso por su id
    if request.method == 'GET':
        serializer = FactSerializer(fact)
        return Response(serializer.data)

    # Actualiza un recurso
    if request.method == 'PUT':
        serializer = FactSerializer(fact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Elimina un recurso
    if request.method == 'DELETE':
        fact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
