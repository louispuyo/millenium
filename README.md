## admin interface 
- create
- delete 
- update 

## user interface 
- create new room starting a new chat 
- see chat getting in the room 
- chatting with other users 

## login requiered for some fonctionalities 

- see all profiles from millenim 
- direct access to the room of each member
- use their username to communicate 

## informations to start 

1 - python3 manage.py makemigrations

2 - python3 manage.py migrate profiles

3 - python3 manage.py runserver

## urls 

### root_url = localhost:8000

- /home/ = see all profile from database and get access to their room 
- /room1/ = access to the room 1
- /room1/?username=paul = access to the room with paul's username 

## script : 

bonjour a tous aujourdhui nous allons essayer de decortiquer le projet pour la candidature openclassroom point par point.
Ce projet rejoins l'idee de creer des canaux d'information en quelques clics. nous allons commencer par parler des models.
grace aux fonctionnalitee django nous sommes en conditions pour travailler avec des bases de donnés sans utiliser le SQL.
donc nous avons des utilisateurs, des messages, et des rooms, chaque message est relier a une room.

avec rooms nous servant de clee etrangere dans messages qui comporte tout comme users un certain nombre de champs.

Nous avons ensuite creer des vues pour nous permettre d'acceder au messages poster ainsi qu'au differents profils des employer de l'entreprise fictive millenium. nous avons creer une application : profiles pour cela

django propose d'utiliser des gabarit distinguer par les balises {{}} et {% %}.
ex : prenons le cas ou je dois afficher les differents profile de mes utilisateur. je vais utiliser la boucle "for" de telle maniere qu'elle m'affiche toute les donnes de l'utilisateur.
je vais devoir ecrire dans mon fichier html 
'{{user.name}}, {{user.bio}}'ect...

Maintenant regardons de plus pret les CRUD de users.
nous avons differents fichiers html appelés template pour recuperer des donnees, en envoyer a la base de donner ainsi qu en supprimer une partie.

les differents profiles sont relier a un tchat qui leurs sont propre.
L'historique des messages sera directement stocker dans une base de donnee.

Regardons comment l'interface admin nous permet de creer plus facilement des objet pour la DB.
on retrouve bien ce que l'on a demander dans admin.py.
ensuite les urls sont ecrit avec un chemin qui utilise des methodes pour 
afficher le bon contenu.

maintenant obsevons de plus pres le code.
on remaque que pour certaine requete nous avons un POST qui a lieu 
il s ecrit de la forme suivant : url/?username=louis si on veut envoyer des donnees vers la base de donnée. 

on peut verifier ca simplement en regardant dans la table correspondante 
faisons un exemple avec la room1 et la room test creer prealablement pour le test. on peut voir que le chat et la creations de nouveau chat fonctionne correctement tant que le serveur tourne avec la commande suivante : python3 manage.py runserver

http://localhost:8000/home/ correspond a notre vue principal
a partir de cette vue qui correspond a home() dans le fichier 
profile/views.py.

a partir de cette vue nous pouvons lire la bio des employée et un lien vers leurs groupe chat, grace a la clee etrangere 'chat' de notre models User dans models.py




