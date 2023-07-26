from django.shortcuts import render, redirect # esto es para los return de cada funcion definida 
from .models import Activaciones, Facturacion
from django.contrib import messages

def index(request):
    # Obtener todos los registros de la tabla Activaciones
    activaciones = Activaciones.objects.all()

    # Pasar los datos al contexto
    context = {
        'activaciones': activaciones,
    }

    return render(request, 'index.html', context)

def login(request):
    # Lógica de la vista para la página de login (si es necesario)
    if request.method == 'POST':
        username = request.POST['username'].strip()  # Eliminar espacios en blanco al principio y al final
        password = request.POST['password'].strip()  # Eliminar espacios en blanco al principio y al final
        
        # Verificar si los campos están vacíos
        if not username or not password:
            # En caso de campos vacíos, mostrar un mensaje de error en el formulario
            messages.error(request, 'Por favor, ingrese usuario y contraseña.')
        elif username == 'admin@admin.com' and password == 'admin':
            # En este caso, la validación es correcta, por lo que redireccionamos a la página index.html
            return redirect('index')
        else:
            # En caso de validación incorrecta, mostramos un mensaje de error en el formulario
            messages.error(request, 'Usuario o clave incorrectos')
    
    context = {
        'titulo': 'Página de login',
    }
    return render(request, 'login.html', context)

def activaciones(request):
    # Obtener todos los registros de la tabla Activaciones
    activaciones = Activaciones.objects.all()

    # Pasar los datos al contexto
    context = {
        'activaciones': activaciones,
    }
    return render(request, 'activaciones.html',context)

def facturacion(request):
    # Lógica de la vista para la página de facturación (si es necesario)
    facturaciones = Facturacion.objects.all()

    # Pasar los datos al contexto
    context = {
        'facturaciones': facturaciones,
    }
    return render(request, 'facturacion.html', context)

def portabilidad(request):
    # Lógica de la vista para la página de portabilidad (si es necesario)
    context = {
        'titulo': 'Página de Portabilidad',
    }
    return render(request, 'portabilidad.html', context)

def creditos(request):
    # Lógica de la vista para la página de créditos (si es necesario)
    context = {
        'titulo': 'Página de Créditos',
    }
    return render(request, 'creditos.html', context)

def cobranzas(request):
    # Lógica de la vista para la página de cobranzas (si es necesario)
    context = {
        'titulo': 'Página de Cobranzas',
    }
    return render(request, 'cobranzas.html', context)

def graficos_activaciones(request):
    # Lógica de la vista para la página de gráficos de activaciones (si es necesario)
    context = {
        'titulo': 'Gráficos de Activaciones',
    }
    return render(request, 'graficos-activaciones.html', context)

def graficos_facturacion(request):
    # Lógica de la vista para la página de gráficos de facturación (si es necesario)
    context = {
        'titulo': 'Gráficos de Facturación',
    }
    return render(request, 'graficos-facturacion.html', context)

def graficos_portabilidad(request):
    # Lógica de la vista para la página de gráficos de portabilidad (si es necesario)
    context = {
        'titulo': 'Gráficos de Portabilidad',
    }
    return render(request, 'graficos-portabilidad.html', context)

def graficos_creditos(request):
    # Lógica de la vista para la página de gráficos de créditos (si es necesario)
    context = {
        'titulo': 'Gráficos de Créditos',
    }
    return render(request, 'graficos-creditos.html', context)

def graficos_cobranzas(request):
    # Lógica de la vista para la página de gráficos de cobranzas (si es necesario)
    context = {
        'titulo': 'Gráficos de Cobranzas',
    }
    return render(request, 'graficos-cobranzas.html', context)

def tableros_activaciones(request):
    # Lógica de la vista para la página de tableros de activaciones (si es necesario)
    context = {
        'titulo': 'Tablero de Activaciones',
    }
    return render(request, 'tableros-activaciones.html', context)

def tableros_facturacion(request):
    # Lógica de la vista para la página de tableros de activaciones (si es necesario)
    context = {
        'titulo': 'Tablero de Facturacion',
    }
    return render(request, 'tableros-facturacion.html', context)