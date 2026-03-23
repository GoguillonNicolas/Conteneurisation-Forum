# Mon Forum Anonyme

## Objectifs du Projet
Ce projet vise à valider les compétences suivantes :
- Comprendre les concepts de base de la conteneurisation Docker afin d'adopter les meilleures pratiques pour déployer et gérer des conteneurs dans divers environnements.
- Créer et utiliser ses propres conteneurs afin de développer, tester et déployer des applications de manière cohérente.
- Création d'une image Docker.
- Mise en place d'un environnement de développement avec Docker Compose.
- Utilisation des Networks et Volumes pour la persistance des données et la sécurité.

## Description du Projet
L'objectif est de concevoir un forum anonyme permettant aux utilisateurs de publier des messages sous un pseudonyme pour interagir avec les autres membres. Aucun système de création de compte/connexion ne sera requis, chaque utilisateur devant utiliser un pseudonyme unique pour communiquer et être identifié.

Dans l'environnement de développement, trois services doivent être développés et une base de données déployée grâce à un Docker Compose :

1. **API** : Gestion de la création et de la récupération des messages du forum. Cette API sera située dans un réseau interne, isolée d'Internet, et pourra interagir avec les autres services.
2. **DB** : Base de données utilisée par l'API pour stocker les messages du forum, également située dans le réseau interne et doit posséder son propre réseau avec l'API pour éviter que Thread et Sender puisse y avoir accès directement.
3. **Thread** : Service chargé d'afficher les messages des utilisateurs via le port 80, consommant les services de l'API.
4. **Sender** : Service chargé d'écrire les messages des utilisateurs via le port 8080, consommant également l'API.

Le choix des technologies pour les services et la base de données est libre.  
Chaque service développé doit être accompagné d'un `Dockerfile` pour générer une image Docker.

Chaque commit doit suivre la convention suivante : **Conventional Commits** pour faciliter la gestion des versions et la génération automatisée des Changelogs (Outil : **Commitizen**).

## Évaluation
Ce projet est individuel. Un lien vers votre dépôt de code est requis pour vérification avant la soutenance.

La soutenance comprendra :
1. Présentation du projet par l'étudiant (environ 7 minutes).
2. Questions sur les choix effectués et revue technique (environ 3 minutes).

L'évaluation se basera sur 20 points, portant sur les compétences évaluées.  
**Le versionnage progressif du code est obligatoire tout au long du projet.**
