from django.shortcuts import render,redirect
from main.models import Produto
from django.shortcuts import redirect,get_object_or_404
import sweetify
from main.forms import ClienteForm,ClienteNewsletterForm,VendaForm,VendedorForm,AddProdutoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    return render(request, "index.html")


def produtos(request):
    lista = Produto.objects.all().order_by('nome')  # ordenando em ordem alfabetica
    # retorna a página de produtos e a lista de objetos tipo Produto
    return render(request, "produtos.html", {'peca':lista})


def quemsomosnos(request):
    return render(request, "quemsomosnos.html")


def detalhes(request, id):  # recuperei o id que foi usado para deixar a url dinamica
    print("ID passado: " + str(id))
    # funciona semelhante a um select - to pegando as informações do produto a partir id
    lista = Produto.objects.get(id=id)
    return render(request, "detalhes.html", {'peca':lista})

def logout_aplicacao(request):
    logout(request)
    return redirect('index')

# FORMS:

@login_required
def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClienteForm()
    else:
        form = ClienteForm()

    return render(request, 'cadastro.html', { 'form' : form})

@login_required
def cadastro_vendedor(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            form = VendedorForm()
    else:
        form = VendedorForm()

    return render(request, 'cadastrovendedor.html', { 'form' : form})

@login_required
def venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            form = VendaForm()
    else:
        form = VendaForm()

    return render(request, 'venda.html', { 'form' : form})

#@login_required
def addproduto(request):
    if request.method == 'POST':
        form = AddProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AddProdutoForm()
    else:
        form = AddProdutoForm()

    return render(request, 'venda.html', { 'form' : form})

#@login_required
def estoque(request):
    lista = Produto.objects.all().order_by('nome')  # ordenando em ordem alfabetica
    # retorna a página de produtos e a lista de objetos tipo Produto
    return render(request, "estoque.html", {'peca':lista})

#@login_required
def update_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    form = AddProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        # Não aparece a mensagem abaixo
        sweetify.sweetalert(request,'Produto alterado com Sucesso!')
        return redirect('estoque')
    
    return render(request, "addproduto.html", {'form':form})

#@login_required
def remover_produto(request, pk):
    produto= get_object_or_404(Produto, pk=pk)
    produto.delete()
    return redirect('estoque')
