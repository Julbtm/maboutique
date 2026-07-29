from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='produits/', blank=True, null=True)
    video = models.FileField(upload_to='produits_videos/', blank=True, null=True)
    disponible = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class Configuration(models.Model):
    numero_whatsapp = models.CharField(max_length=20, help_text="Format international sans + ni espaces, ex: 22990000000")

    def __str__(self):
        return f"Configuration ({self.numero_whatsapp})"

    def save(self, *args, **kwargs):
        # Empêche d'avoir plusieurs lignes de configuration — une seule ligne autorisée
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_numero(cls):
        config, created = cls.objects.get_or_create(pk=1, defaults={'numero_whatsapp': '22900000000'})
        return config.numero_whatsapp