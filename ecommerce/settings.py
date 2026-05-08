"""
Django settings for ecommerce project.
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = "django-insecure-=@3*+f8@gw7792$!(9b^uu&l8i2)hpbjfuq%ff9@sma!@*z9#("

DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'products',
    'accounts'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ecommerce.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ecommerce.wsgi.application"

# Database
# Configuration pour MySQL (XAMPP)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_ecommerce',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "fr-fr" # Mis en français pour ton projet
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'images')

# ==============================================================================
# --- PATCHES DE COMPATIBILITÉ POUR MARIADB (XAMPP) ---
# Ces lignes permettent à Django 6.0+ de fonctionner avec MariaDB < 10.6
# ==============================================================================

from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.mysql.base import DatabaseWrapper as MySQLDatabaseWrapper

# 1. Désactiver la vérification stricte de la version de la base de données
BaseDatabaseWrapper.check_database_version_supported = lambda self: None

# 2. Désactiver les fonctionnalités "RETURNING" non supportées par MariaDB 10.4
# On utilise features_class pour impacter toutes les futures connexions
MySQLDatabaseWrapper.features_class.can_return_columns_from_insert = False
MySQLDatabaseWrapper.features_class.can_return_rows_from_bulk_insert = False
# ==============================================================================

LOGIN_REDIRECT_URL = "profile"     # Vers le profil après connexion
LOGOUT_REDIRECT_URL = "product_list" # Vers l'accueil après déconnexion
LOGIN_URL = "login"                # Page par défaut si accès refusé