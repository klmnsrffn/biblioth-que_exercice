import connecter
from administrateur import homepage as homepage

# Menu pour les administrateurs
def admin_menu():
    while True:
        print("\nMenu administrateur :")
        print("1. Créer un utilisateur")
        print("2. Supprimer un utilisateur")
        print("3. Lister les utilisateurs")
        print("4. Quitter")
        choice = input("Votre choix : ")
        if choice == "1":
            while True:
                username = input("Nom d'utilisateur : ")
                if not username:
                    print("Vous pouvez entrer nom d'utilisateur. Program sont terminer")
                    break
                password = input("Mot de passe : ")
                if not password:
                    print("Vous pouvez entrer mot de passe. Program sont terminer")
                    break
                if ' 'in username:
                    print("Le nom d'utilisateur ne peut pas contenir des espaces.")
                elif ' ' in password:
                    print("Le mot de passe ne peut pas contenir des espaces.")
                    break
            if username and password:
                admin = input("Administrateur ? (o/n) ").lower()
                while True:
                    if admin == "o":
                        admin = True
                        connecter.create_user(username, password, admin)
                        print(f"Utilisateur '{username}' créé avec succès.")
                        break
                    elif admin == "n":
                        admin = False
                        connecter.create_user(username, password, admin)
                        print(f"Utilisateur '{username}' créé avec succès.")
                        break
                    else:
                        print("Choix invalide. Veuillez réessayer.")
                        admin = input("Administrateur? (o/n)").lower()
            else:
                print("Choix invalide. Veuillez réessayer.")
        elif choice == "2":
            username = input("Nom d'utilisateur à supprimer : ")
            connecter.delete_user(username)
        elif choice == "3":
            connecter.list_users()
        elif choice == "4":
            break
            homepage.homepage_menu
        else:
            print("Choix invalide.")

