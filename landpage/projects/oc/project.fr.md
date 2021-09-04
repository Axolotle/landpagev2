---
title: Objets Célestes
tree:
    - name: Objets Célestes
      status: progress
      children:
        - name: Constellations
          status: done
          text: Modélisation de 8 constellations aux formats .dae & .stl.
          children:
            - name: 5 – Cetus
            - name: 38 – Ursa Major
            - name: 42 – Hydra
            - name: 53 – Microscopium
            - name: 73 – Norma
            - name: 77 – Sculptor
            - name: 80 – Mensa
            - name: 82 – Telescopium
        - name: Cartes
          status: done
          text: Propositions et reprises de dessins se référant aux noms des constellations.
        - name: Impressions 3D
          status: done
          text: Prototypages d'impressions 3D des volumes à échelle extrêmement réduites.
        - name: Exo Grande Ours
          status: done
          text: Carte de l'anamorphose de la Grande Ourse vue depuis Gliese 667C.
        - name: Volume céleste
          status: none
          text: Matérialisation du volume global de toutes les constellations assemblées.
        - name: Atlas
          status: none
          text: Édition d'un atlas du ciel
        - name: Exo-atlas
          status: none
          text: Sélectionner une exoplanète potentiellement propice à la vie, repérer ses étoiles les plus brillantes et tenter d'inventer ses constellations.
---
---note
Le projet était interrompu depuis 2014 au stade de prototype pour 8 constellations.  
Je suis actuellement en train de développer une carte du ciel 3D dans laquelle on pourra se déplacer, observer et dessiner des [asterismes](https://fr.wikipedia.org/wiki/Ast%C3%A9risme).  
Seules les étoiles de la constellation *Ursa Majoris* sont présentes d'après les données d'[Hipparcos](https://fr.wikipedia.org/wiki/Hipparcos) accessibles via [Simbad](http://simbad.u-strasbg.fr/simbad/), il faut que je me documente davantage sur la récupération des données du satellite [Gaia](https://fr.wikipedia.org/wiki/Gaia_(satellite)) dont le catalogue final est attendu pour 2020.

---tldr
Redonner aux constellations leur 3<sup>e</sup> dimension en les modélisant sous forme de petits volumes à partir des données recueillies par le satellite [Hipparcos](https://fr.wikipedia.org/wiki/Hipparcos).

---box
**Parutions : Code 2.0**

Une petite double page dans [Code 2.0](http://www.codemagazine.fr/) vous propose de dessiner la Grande Ourse vue depuis l'exoplanète Gliese 667C.


---
![titre graphique de Objets Célestes](titre.svg){.title}

Les dessins des constellations tels que nous les connaissons appartiennent à une époque révolue ; ils ne sont que la simple anamorphose d’un tracé beaucoup plus complexe qu'il est désormais possible de mettre en lumière.  
En récupérant la position des étoiles d'une constellation par rapport au Soleil, il est possible de modéliser un volume à facettes dont chaque sommet sera associé à la position « exacte » – d’après nos actuelles observations issues des calculs du satellite [Hipparcos](https://fr.wikipedia.org/wiki/Hipparcos) – de chacune des étoiles dans l'espace. Libérée du point de vue terrestre, la constellation retrouve dès lors sa troisième dimension.

![Grande Ourse en 3D](vue3D.png)
*modélisation de la Grande Ourse*


Grâce à cette modélisation, de nouvelles formes et traductions sont envisageables : matérialiser les constellations grâce à une impression 3D à échelle extrêmement réduite, tenant dans la main ; associer en un volume global toutes les constellations et produire ainsi une carte/objet en trois dimensions de la sphère céleste ; ou encore, observer la déformation opérée par l’anamorphose d'un point de vue autre que celui de la Terre.

![Schéma de la Grande Ourse](map.svg)
*dessin de la Grande Ourse*


Il n'existe pas de convention ni de sélection officielle d'étoiles définissant le dessin d'une constellation.  
La sélection des étoiles pour ce projet suit une méthode basique, chacune des étoiles possède une magnitude inférieure à 6 (au delà une étoile n'est pas visible à l'oeil nu) et sélectionne arbitrairement un nombre suffisant d'objets dans l'ordre de leur magnitude (aucune étoile ayant une magnitude inférieure à la plus faible n'a été rejetée) afin de trouver un dessin littéralement similaire à leur nom. La modélisation 3D est elle aussi arbitraire quoique générique (les faces partant du Soleil tentent d'englober l'ensemble d'étoiles et se referment derrière).
