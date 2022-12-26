from django.contrib import admin
from main.models import Cliente,Vendedor,Produto

admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Produto)

class VendaAdmin (admin.ModelAdmin):
    list_display =['Cliente','Vendedor']
    