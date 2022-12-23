"""principal URL Configuration

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
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from main.views import logout_aplicacao

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', index,name="index"),
    path('produtos/',produtos,name="produtos"),
    path('quemsomosnos/',quemsomosnos,name="quemsomosnos"),
    path('detalhes/<int:id>',detalhes,name="detalhes"),
    path('cadastro/',cadastro_cliente,name='cadastro'),
    path('venda/',venda,name='venda'),
    path('addproduto/',addproduto,name='addproduto'),
    path('cadastrovendedor/',cadastro_vendedor,name='cadastrovendedor'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',logout_aplicacao,name='logout'),
    path('estoque/',estoque,name='estoque'),
    path('editar/<int:pk>/', update_produto, name='editar_produto'),
    path('remover/<int:pk>/', remover_produto, name='remover_produto'),
    path('registro_vendas', registro_vendas, name='registro_vendas'),
#tem que colocar virgula depois da última url
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



