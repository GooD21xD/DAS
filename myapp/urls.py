"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('activaciones/', views.activaciones, name='activaciones'),
    path('facturacion/', views.facturacion, name='facturacion'),
    path('portabilidad/', views.portabilidad, name='portabilidad'),
    path('creditos/', views.creditos, name='creditos'),
    path('cobranzas/', views.cobranzas, name='cobranzas'),
    path('graficos-activaciones/', views.graficos_activaciones, name='graficos-activaciones'),
    path('graficos-facturacion/', views.graficos_facturacion, name='graficos-facturacion'),
    path('graficos-portabilidad/', views.graficos_portabilidad, name='graficos-portabilidad'),
    path('graficos-creditos/', views.graficos_creditos, name='graficos-creditos'),
    path('graficos-cobranzas/', views.graficos_cobranzas, name='graficos-cobranzas'),
    path('tableros-activaciones/', views.tableros_activaciones, name='tableros-activaciones'),
    path('tableros-facturacion/', views.tableros_facturacion, name='tableros-facturacion'),
]
