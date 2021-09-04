---
tree:
    - name: pixelpath
      status: progress
      children:
        - name: Caractères
          status: done
          text: Dessin des caractères de la table Latin-1 ([ISO/CEI 8859-1](https://fr.wikipedia.org/wiki/ISO/CEI_8859-1)).
          children:
            - name: Romain
            - name: Italique
        - name: Police de caractère version Alpha
          status: done
        - name: Police de caractère
          status: progress
          text: Police générée automatiquement en italique ou romain.

gallery:
    - multiple:
        - uri: pxphTable1.png
          alt: Première partie du set de caractères Pixelpath
        - uri: pxphTable2.png
          alt: Deuxième partie du set de caractères Pixelpath
      caption: Tous les caractères dessinés pour pxph.
    - uri: pixelSpecimen.png
      crisp: True
      class: fullw
      caption: version bitmap.
    - uri: process.png
      caption: Principe du dessin.
    - uri: paths.jpg
      caption: Sets de caractères en pixel puis transformés en *path*.

---
---note
J'aimerais revoir la génération des fontes avec un nouveau programme fait main car les précédentes versions avaient été réalisées sous logiciel propriétaire. L'idée serait de pouvoir générer une police avec l'épaisseur et le style de contour souhaité, en romain ou italique. L'avancement peut être vu sur ce [*repo*](https://github.com/Axolotle/pixel2path).

---tldr
Police de caractère de titrage (mais que j'utilise aussi pour du texte de labeur) dont le principe consiste à convertir des caractères fais de pixel en chemin vectoriel.

---
![Titraille en image des lettres PXPH](pxphTitre.svg){.title}

*Pixelpath-9* est une font de titrage pixel transposée en son équivalent vectoriel.

À l'origine développée pour *light-nanosecond ruler* dans ce même jeu de passage entre matriciel et vectoriel, la version pixel répond à la contrainte de produire un dessin lisible avec le moins de pixels possible (une grille de 9 × 5 px au total pour des caractères classiques de 5 × 3 px) ; la version vectorielle en est une simple traduction : un tracé vectoriel passe par le centre (théorique) de chaque pixel afin de proposer une typo linéale.

![Pangramme](pxphPagramme.png)

Une *italic* existe ainsi qu'une version avec une grille de 14 × 7 px mais il me faudrait les retravailler.

![Pangramme italique](pxphItalPangramme.png)
