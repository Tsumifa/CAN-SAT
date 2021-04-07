# CAN-SAT
### Description générale :
Le CAN-SAT est un concours organisé par l'ESA (Agence Spatiale Européenne) dont le but est de créer un satellite de la taille d'une canette.
Le dossier contient l'application de traitement des données collectées en vol.

 **Les Données Collectées et leurs mode d’analyse :**
| Type de Donnée | Module d'analyse |
|--|--|
| GPS : Latitude; Longitude; Vitesse; Nombre de Satellite; Qualité du signal | `Folium` `Matplotlib` |
|Température; Pression; altitude|`Matplotlib`|
|Accéléromètre : Accélération X; Accélération Y; Accélération Z|`Matplotlib` |
|Vidéos : Caméra classique; Caméra thermique|`OpenCV`|

Auteur: @Tsumifa.
Lien vers le projet : [Site web](https://lc-sat.github.io/doc/software) [Github](https://github.com/LC-Sat) [Discord](https://discord.gg/Zs9HMcUNxx) [Twitter](https://twitter.com/lc_sat) [Youtube](https://www.youtube.com/channel/UCol3odMUuW2hn6GGNrv9VLA)
 
### Informations techniques :
L 'application est développée avec le langage `Python`.
Infrastructure MVC (Models Views Controllers) pour l'interface.
