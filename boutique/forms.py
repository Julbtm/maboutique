from django import forms
from .models import Produit, Configuration

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'image', 'disponible']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du produit'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 4}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix en FCFA'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = ['numero_whatsapp']
        widgets = {
            'numero_whatsapp': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 22990000000'
            }),
        }