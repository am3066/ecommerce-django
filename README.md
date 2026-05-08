# 🛍️ E-Commerce Django — Atelier 3

Projet e-commerce avec système d'authentification Django.

## Fonctionnalités
- Liste et détail des produits
- Inscription / Connexion / Déconnexion
- Page profil protégée
- Page panier protégée
- Interface d'administration Django

## Installation

```bash
# Cloner le projet
git clone https://github.com/TON_USERNAME/ecommerce-django.git
cd ecommerce-django

# Créer l'environnement virtuel
python -m venv myenv
myenv\Scripts\activate  # Windows
source myenv/bin/activate  # Linux/macOS

# Installer les dépendances
pip install -r requirements.txt

# Migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
```

## Structure