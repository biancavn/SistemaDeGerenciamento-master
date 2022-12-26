from django import forms
from main.models import Cliente,Vendedor,Produto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {
            'data_nascimento': forms.TimeInput(attrs={'type':'date'}),
            'sexo': forms.RadioSelect(),
        }

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'

        widgets = {
            'data_nascimento': forms.TimeInput(attrs={'type':'date'}),
            'sexo': forms.RadioSelect(),
        }

class AddProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
