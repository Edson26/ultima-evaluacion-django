"""LocalGastronomico URL Configuration

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
from reservas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('crearInscripcion/', views.crearInscripcion, name="crearInscripcion"),
    path('crearInstituto/', views.crearInstituto, name="crearInstituto"),
    path('listaInscritos/', views.listadoInscrito, name="listaInscripcion"),
    path('listaInstitutos/', views.listadoInstituto, name="listaInstituto"),
    path('editarInscripcion/', views.editarInscrito, name="editarInscripcion"),
    path('editarInstituto/', views.editarInstituto, name="editarInstituto"),
    # Esto falta por crear
    # path('api1/', views.api1, name="api1")
    # path('api2/', views.api2, name="api2")
]
