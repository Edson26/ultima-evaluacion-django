"""django_taller_final URL Configuration

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
from seminario import views
from Api_Rest import views as viewsApi
from Funcion_Based_Views import views as viewsFuncion
from Class_Based_Views import views as viewsClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('listado/', views.listado, name="listado"),
    path('api/inscritos/', viewsApi.verinscritos, name="api_rest"),
    path('api/funcion/', viewsFuncion.listar_institucion, name="api_funcion"),
    path('api/funcion/detalle/<int:pk>', viewsFuncion.detalle_institucion, name="api_funcion_detalle"),
    path('api/class', viewsClass.ListaInscritos.as_view(), name="api_class"),
    path('api/class/detalle/<int:pk>', viewsClass.DetalleInscritos.as_view(), name="api_class_detalle"),
    path('crearInscripcion/', views.crearInscripcion, name="crearInscripcion"),
    path('crearInstitucion/', views.crearInstitucion, name="crearInstitucion"),
    path('listaInscritos/', views.listadoInscrito, name="listaInscripcion"),
    path('listaInstituciones/', views.listadoInstitucion, name="listaInstituciones"),
    path('editarInscripcion/<int:id>', views.editarInscrito, name="editarInscripcion"),
    path('editarInstitucion/<int:id>', views.editarInstitucion, name="editarInstitucion"),
    path('eliminarInscripcion/<int:id>', views.eliminarInscripcion,name="eliminarInscripcion"),
    path('eliminarInstitucion/<int:id>', views.eliminarInstitucion, name="eliminarInstitucion"),
    # Esto falta por crear
    # path('api1/', views.api1, name="api1")
    # path('api2/', views.api2, name="api2")
]
