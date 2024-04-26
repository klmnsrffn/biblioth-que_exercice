## Vue d'ensemble
Ce projet est un système de gestion de bibliothèque simple. Les administrateurs et les utilisateurs réguliers peuvent se connecter via la même page de connexion, mais ils seront dirigés vers différentes fonctionnalités en fonction de leur type de compte (administrateur ou utilisateur régulier).

##Fonctionnalités pour les administrateurs :
Créer des comptes pour les administrateurs et les utilisateurs réguliers
Supprimer des comptes existants
Ajouter de nouveaux livres à la bibliothèque
Utiliser les fonctionnalités d'emprunt et de retour de livres

## Fonctionnalités pour les utilisateurs réguliers :
Emprunter des livres de la bibliothèque
Retourner des livres empruntés

## Comment ça fonctionne ?
Lors de l'accès au système, les utilisateurs seront invités à se connecter.
Après une connexion réussie, les administrateurs auront accès aux fonctionnalités administratives mentionnées ci-dessus, tandis que les utilisateurs réguliers n'auront accès qu'aux fonctionnalités d'emprunt et de retour de livres.
Les administrateurs peuvent gérer les comptes, ajouter de nouveaux livres à la bibliothèque et gérer les opérations d'emprunt et de retour de livres.
Les utilisateurs réguliers peuvent parcourir les livres disponibles et les emprunter ou les retourner selon les besoins.

## Fonctionnalités pour les administrateurs
Après s'être connectés, les administrateurs seront invités à choisir entre la gestion des comptes ou la gestion des livres de la bibliothèque.
Gérer les comptes

1. Créer un compte
Les administrateurs peuvent créer des comptes pour d'autres administrateurs ou utilisateurs réguliers.
Les champs du nom d'utilisateur et du mot de passe ne peuvent pas être laissés vides ou contenir uniquement des espaces.

2. Supprimer un compte
Les administrateurs ont la possibilité de supprimer des comptes existants.
3. Afficher tous les comptes
Les administrateurs peuvent afficher une liste de tous les comptes enregistrés dans la base de données.

Gérer les livres de la bibliothèque

1. Ajouter un nouveau livre
Les administrateurs peuvent ajouter de nouveaux livres à la bibliothèque.
Les champs du titre et de l'auteur du livre ne peuvent pas être laissés vides.
La quantité du livre doit être remplie avec un entier positif.

2. Emprunter et retourner des livres
Les administrateurs peuvent emprunter et retourner des livres, tout comme les utilisateurs réguliers.

4. Afficher la liste des livres
Les administrateurs peuvent afficher une liste de tous les livres disponibles dans la bibliothèque.


* Validation et gestion des erreurs
Des contrôles de validation appropriés sont en place pour s'assurer que les champs requis ne sont pas laissés vides ou remplis avec des données invalides.
Des messages d'erreur seront affichés pour guider les utilisateurs en cas de saisie ou d'opérations invalides.


* Intégration de la base de données
Toutes les données des comptes et des livres sont stockées et récupérées de manière sécurisée dans une base de données, assurant la persistance et l'intégrité des données.
Fonctionnalités pour les utilisateurs réguliers
Après s'être connectés, les utilisateurs réguliers auront accès aux fonctionnalités suivantes :


1. Afficher la liste des livres
Les utilisateurs réguliers peuvent voir une liste de tous les livres disponibles dans la bibliothèque.
La liste des livres fournira des informations sur la disponibilité de chaque livre, indiquant s'il est actuellement en stock ou emprunté.


2. Emprunter un livre
Les utilisateurs réguliers peuvent emprunter des livres de la bibliothèque.
Le système s'assurera qu'un livre est disponible avant de permettre son emprunt.
Des contrôles de validation appropriés seront en place pour empêcher les utilisateurs d'emprunter un livre qui est déjà emprunté par un autre utilisateur.


3. Retourner un livre
Les utilisateurs réguliers peuvent retourner les livres qu'ils ont précédemment empruntés.
Lors du retour d'un livre, le système mettra à jour le statut de disponibilité du livre, le rendant accessible pour que d'autres utilisateurs puissent l'emprunter.


* Limitations
Les utilisateurs réguliers n'auront pas accès aux fonctionnalités administratives, telles que la création ou la suppression de comptes, l'ajout de nouveaux livres ou la gestion des comptes d'autres utilisateurs. Ces fonctionnalités sont réservées aux administrateurs pour maintenir l'intégrité et la sécurité du système de gestion de la bibliothèque.

## Organigramme

### Page d'Accueil
![main_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/aa9effec-d927-45d6-ab3b-365270e60091)


### Database
![database_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/8d57d2c3-3f2b-4041-9d2e-e8a6fa6d5566)


### Se Connecter
![login_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/4316c991-e66b-4764-bd32-69b99342207d)


### Page d'Accueil d'Administrateur
![homepage_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/98e820c1-1bb2-4896-9c90-94a8d5a9f61f)


### Gêrer des comptes
![account_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/1773722f-4839-4e40-9bcb-0e0c045c5498)


### Gérer des livres
![book_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/944391b3-43c0-4647-95f8-8d1c7ad5497e)


### Page d'Accueil d'Utilisateur
![user_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/db156d94-5748-48ed-bb9f-19bfe490c3c2)

### Interface d'Utilisateur
![user_book_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/f838fea7-cbd6-480b-ad9c-a3824475a34b)
