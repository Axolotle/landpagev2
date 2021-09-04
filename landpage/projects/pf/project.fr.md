---
title: Formats Planétaires
tree:
    - name: formats planétaires
      status: progress
      children:
        - name: Formats
          status: done
          text: Pour chacune des 8 planètes du Système Solaire, a été définie une série de formats de papier au ratio 1:√2
          children:
            - name: Ε (epsilon) - Mercure
            - name: Α (alpha) – Vénus
            - name: Γ (gamma) – Terre
            - name: α (alpha minor) – Mars
            - name: Ζ (zêta) – Jupiter
            - name: Κ (kappa) – Saturne
            - name: Ο (omicron) – Uranus
            - name: Π (pi) - Neptune
        - name: Site web
          status: done
          text: Un site présentant les formats accompagnés d'un dispositif de visualisation et proposant des versions papier en téléchargement.
        - name: Édition
          status: progress
          text: Génération d'un catalogue sous forme de classeur à partir des différentes données sur les formats. Chaque planète dispose de son intercalaire, d'un nombre de pages équivalent au nombre de formats de la série imprimé sur papier calque et d'une fiche récapitulative.

gallery:
    - uri: posterSpirale.png
      class: fullw
      caption: Représentations selon différentes méthodes des rapports entre les formats inférieurs au Γ49 (équivalent A0).
    - multiple:
        - uri: earthExcerpt1.jpg
          alt: Couverture d'intercalaire comparant le sphéroïde terrestre et son équivalent à plat.
        - uri: earthExcerpt2.jpg
          alt: Interieur de couverture avec quelques informations sur la série.
        - uri: earthExcerpt3.jpg
          alt: Première page affichant les données du format 0.
        - uri: earthExcerpt4.jpg
          alt: Format 53
        - uri: earthExcerpt5.jpg
          alt: Format 55
        - uri: earthExcerpt6.jpg
          alt: Format 57
      caption: Quelques pages de la série gamma (Γ => Terre).
---
---note
Le site et les versions imprimables sont prêtes, mais le catalogue n'a pas encore été imprimé.


---tldr
Retranscrire la superficie d'une planète en une série de formats de papier rectangulaires dont le rapport entre la largeur et la longueur est 1:√2 à l'instar de la série A ([ISO 216](https://fr.wikipedia.org/wiki/ISO_216) : A0, A1, etc.)


---
Pour chaque planète du Système solaire est défini un format de référence — dit 0 préfixé de sa lettre grecque — de ratio 1:√2 arrondi au millimètre et dont l'aire est égale à celle de cette planète.  
Sont ensuite récursivement calculés tous les formats de la série en divisant la précédente longueur par 2 et en récupérant la précédente largeur comme nouvelle longueur (L = longueur / 2 ; l = largeur) jusqu'à atteindre un format pouvant être apposé dans un format A0 suivi de onze de ses prochaines divisions.

![rapport de taille entre les planètes](rapportTailles.png)

Les formats de papier 1:√2 ont la particularité de conserver ce ratio à chaque division — pas exactement cependant car le résultat de chaque division est arrondie au millimètre inférieur —, il est ainsi possible de contenir deux formats 1 en orientation paysage dans un format 0 en orientation portrait, quatre formats 2 (portrait) dans un format 0 (portrait), etc.  
Les approximations induites par les arrondis produisent des pertes négligeables dans le cas de la série A mais il en est tout autrement pour les formats planétaires.

![Format Ζ60](jupiter60.jpg)
*Format 60 de la série Ζ (jupiter)*

Sur le site, vous trouverez les dimensions de chacun des formats planétaires ainsi que ses divisions.  
Une version papier imprimable sous forme de catalogue est aussi téléchargeable. Celle-ci présente sur chacune de ses pages la prochaine division, ses dimensions et quelques autres informations. Le catalogue est imprimé dans le premier format planétaire apposable sur un A4, ainsi tous les formats sont à échelle 1 à partir de celui-ci (Ε51, Α53, Γ53, α52, Ζ60, Κ60, Ο57 et Π57).
