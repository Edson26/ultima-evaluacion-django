from django.contrib import admin
from .models import Inscritos, Institucion
# Register your models here.


class InscritosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'fecha', 'hora', 'institucion','estado','observacion']


admin.site.register(Inscritos, InscritosAdmin)


class InstitucionAdmin(admin.ModelAdmin):
    list_display = ['nombre']


admin.site.register(Institucion, InstitucionAdmin)
