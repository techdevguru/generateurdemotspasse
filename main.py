import random
import string

def generate_password(length):
    """Génère un mot de passe aléatoire de la longueur donnée."""
    characters = string.printable.strip()
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def get_int_input(prompt):
    """Demande un entier à l'utilisateur jusqu'à ce qu'une entrée valide soit fournie."""
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Veuillez entrer un nombre entier positif.")
            else:
                return value
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

def get_yes_no_input(prompt):
    """Demande une entrée oui/non à l'utilisateur jusqu'à ce qu'une entrée valide soit fournie."""
    while True:
        value = input(prompt).strip().lower()
        if value in ('o', 'oui'):
            return True
        elif value in ('n', 'non'):
            return False
        else:
            print("Veuillez entrer 'oui' ou 'non'.")

if __name__ == '__main__':
    print("Bienvenue dans le générateur de mots de passe aléatoires !")

    num_passwords = get_int_input("Combien de mots de passe souhaitez-vous générer ? ")

    length = get_int_input("Combien de caractères voulez-vous dans votre mot de passe ? ")

    include_special_chars = get_yes_no_input("Voulez-vous inclure des caractères spéciaux dans vos mots de passe ? (oui/non) ")
    if include_special_chars:
        characters = string.printable.strip()
    else:
        characters = string.ascii_letters + string.digits

    passwords = [generate_password(length) for i in range(num_passwords)]

    print("\nVoici vos mots de passe :")
    for password in passwords:
        print(password)

    save_to_file = get_yes_no_input("\nVoulez-vous enregistrer ces mots de passe dans un fichier ? (oui/non) ")
    if save_to_file:
        filename = input("Nom du fichier : ")
        with open(filename, 'w') as f:
            f.write('\n'.join(passwords))
            print(f"\nLes mots de passe ont été enregistrés dans le fichier {filename}.")
