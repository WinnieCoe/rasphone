# rasphone (Work In Progress...)
Transformation d'un vieux téléphone à touches Socotel en livre d'or audio

- Carte Raspberry Pi (B+ / 3B+ / 4 / Zéro W) => Tests en cours sur quelle carte sera retenue...
- Microphone USB
- Mini-jack
- Pour le Zéro W, création d'un mini-circuit de filtrage pour utiliser la broche GPIO 18 en sortie audio
- Téléphone Socotel S63 à touches


Démontage du téléphone et de ses composants (parti pris de ne pas rendre réversible le procédé ==> à voir si cela sera possible une fois l'ensemble développé)
Adaptation de la platine du téléphone pour y intégrer les points de connexion nécessaires
Intégration du Raspberry dans le boitier
Connexion au microphone à charbon original en utilisant une partie du schéma d'origine (transformateur + résistances + condensateur) vers la carte microphone USB
Connexion au clavier à chiffre matriciel sur GPIO
Connexion à l'interrupteur du combiné


Programmation et principe de fonctionnement : 
- Surveillance de l'état de l'interrupteur du combiné
- Tant que raccroché => Mise en veille
- Lorsque décroché => Passage en état actif, lancement d'un audio d'accueil préenregistré avec menu principal
- Si appui sur 0 : interruption de toute action, retour au menu principal
- Si appui sur 1 : lecture d'un audio préenregistré et début d'un menu alternatif (plusieurs numéros et pistes audios pour revenir ensuite au menu)
- Si appui sur 2 : lecture d'un audio préenregistré et démarrage d'un enregistrement audio de 1min maximum dans un répertoire dédié
- Si appui sur 3 : lecture d'un audio préenregistré et sélection aléatoire d'un enregistrement audio dans le répertoire dédié
- Si appui sur 9 puis 8 puis 7 : extinction du Raspberry
- Si pendant l'une de ces actions (sauf l'extinction), le combiné est raccroché, interruption de toute action et remise en veille

Difficultés rencontrés dans la programmation :
Surveillance avec add.event.detect sur front montant puis descendant, sur les deux fronts => Erreur rencontrée avec runtimeerror : failed to add edge detection ??


