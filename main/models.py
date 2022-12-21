from django.db import models

# Create your models here.

LISTA_SEXO= [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino')
]

class ClienteNewsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    CPF = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=150, choices=LISTA_SEXO)
    email = models.EmailField()
    endereço = models.CharField(max_length=150)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=150)
    CPF = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=150, choices=LISTA_SEXO)
    email = models.EmailField()
    endereço = models.CharField(max_length=150)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    valor = models.DecimalField('Preço do produto', max_digits=8, decimal_places=2) #alteração no tipo de models
    descricao_produto = models.TextField()
    quantidade_produto = models.IntegerField()
    imagem = models.ImageField(upload_to='main')
    
    def __str__(self):
        return f'{self.nome}' ' - ' f' Valor: R$ {self.valor}'

class Venda(models.Model):
    data = models.DateTimeField()
    quantidade_venda = models.FloatField()
    valor_total = models.FloatField()
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Vendedor = models.ManyToManyField(Vendedor)
    Produto = models.ManyToManyField(Produto)

    def __str__(self):
        return f'Horário: {self.data}' ' - ' f'Cliente: {self.Cliente}'

