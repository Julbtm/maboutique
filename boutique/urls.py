from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('produits/', views.liste_produit, name='liste_produit'),
    path('a-propos/', views.apropos, name='apropos'),
    path('contact/', views.contact, name='contact'),

    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),

    path('gestion/', views.admin_produits, name='admin_produits'),
    path('gestion/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('gestion/modifier/<int:id>/', views.modifier_produit, name='modifier_produit'),
    path('gestion/supprimer/<int:id>/', views.supprimer_produit, name='supprimer_produit'),
    path('gestion/configuration/', views.modifier_configuration, name='modifier_configuration'),
]