from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Produit, Configuration
from .forms import ProduitForm, ConfigurationForm

# --- Pages publiques ---

def accueil(request):
    return render(request, 'boutique/accueil.html')

def liste_produit(request):
    produits = Produit.objects.filter(disponible=True)
    return render(request, 'boutique/liste.html', {
        'produits': produits,
        'whatsapp_number': Configuration.get_numero(),
    })

def apropos(request):
    return render(request, 'boutique/apropos.html')

def contact(request):
    return render(request, 'boutique/contact.html', {
        'whatsapp_number': Configuration.get_numero(),
    })

# --- Connexion / déconnexion ---

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_produits')
        else:
            messages.error(request, "Identifiants incorrects.")
    return render(request, 'boutique/connexion.html')

def deconnexion(request):
    logout(request)
    return redirect('accueil')

# --- Tableau de bord admin (protégé) ---

@login_required
def admin_produits(request):
    produits = Produit.objects.all()
    return render(request, 'boutique/admin_produits.html', {'produits': produits})

@login_required
def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit ajouté avec succès.")
            return redirect('admin_produits')
    else:
        form = ProduitForm()
    return render(request, 'boutique/produit_form.html', {'form': form, 'titre': 'Ajouter un produit'})

@login_required
def modifier_produit(request, id):
    produit = get_object_or_404(Produit, id=id)
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit modifié avec succès.")
            return redirect('admin_produits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'boutique/produit_form.html', {'form': form, 'titre': 'Modifier le produit'})

@login_required
def supprimer_produit(request, id):
    produit = get_object_or_404(Produit, id=id)
    if request.method == 'POST':
        produit.delete()
        messages.success(request, "Produit supprimé.")
        return redirect('admin_produits')
    return render(request, 'boutique/confirmer_suppression.html', {'produit': produit})

# --- Configuration (numéro WhatsApp) ---

@login_required
def modifier_configuration(request):
    config, created = Configuration.objects.get_or_create(pk=1, defaults={'numero_whatsapp': '22900000000'})
    if request.method == 'POST':
        form = ConfigurationForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            messages.success(request, "Numéro WhatsApp mis à jour.")
            return redirect('admin_produits')
    else:
        form = ConfigurationForm(instance=config)
    return render(request, 'boutique/configuration.html', {'form': form})