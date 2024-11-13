import subprocess
import sys

# Fonction pour installer les packages depuis un fichier
def install_packages_from_file(file_path):
    with open(file_path, "r") as file:
        packages = file.readlines()
    
    # Installer chaque package
    for package in packages:
        package = package.strip()  # Enlever les espaces et les retours à la ligne
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Package {package} installé.")

# Appeler la fonction avec le fichier contenant les packages
if __name__ == "__main__":
    install_packages_from_file("packages.txt")
