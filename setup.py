from setuptools import setup

setup(
    install_requires=[  # Liste des dépendances externes à installer
        "easyocr",   # Utilisé pour la reconnaissance de texte
        "requests",  # Pour effectuer des requêtes HTTP
        "fuzzywuzzy",  # Pour la comparaison de chaînes de caractères
    ]
)
