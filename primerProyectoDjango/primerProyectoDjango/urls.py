"""primerProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from webapp.views import bienvenido, despedida, listar_alumnos
from deportes.views import deportes, listar_selecciones, anadir_selecciones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name="inicio"),
    path('goodbye/', despedida),
    path('deportes/', deportes, name="deportes"),
    path('alumnos/listar_alumnos/', listar_alumnos, name="listado_alumnos"),
    path('deportes/futbol/listado-selecciones', listar_selecciones, name="listado_selecciones"),
    path('deportes/futbol/anadir-selecciones', anadir_selecciones, name="anadir_selecciones"),
]
