from django import forms
from main.models import Cliente,ClienteNewsletter,Venda,Vendedor,Produto

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

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'

        widgets = {
            'data': forms.TimeInput(attrs={'type':'date'}),
            'produto': forms.CheckboxSelectMultiple(),
        }

class AddProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

        widgets = {
            
        }

class ClienteNewsletterForm(forms.ModelForm):
    class Meta:
        model = ClienteNewsletter
        fields = '__all__'