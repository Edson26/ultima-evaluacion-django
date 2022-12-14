from django.contrib import admin
from .models import Inscritos, Instituto
# Register your models here.


class InscritosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'fecha', 'hora', 'institucion']


admin.site.register(Inscritos, InscritosAdmin)


class InstitutoAdmin(admin.ModelAdmin):
    list_display = ['nombre']


admin.site.register(Instituto, InstitutoAdmin)
