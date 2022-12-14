from django.contrib import admin
from main.models import Cliente,Vendedor,Venda,Produto,ClienteNewsletter
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(ClienteNewsletter)

class VendaAdmin (admin.ModelAdmin):
    list_display =['Cliente','Vendedor']
    