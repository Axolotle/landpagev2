---
tree:
    - name: Sisifont
      status: done
      children:
        - name: Caractères
          text: Dessin des caractères de la table Latin-1 ([ISO/CEI 8859-1](https://fr.wikipedia.org/wiki/ISO/CEI_8859-1)).
        - name: Générateurs
          text: Générateurs (python ou js) permettant de convertir du texte en Sisifont.
---
---tldr
Police de caractère de type *ANSI art* utilisant les caractères de boîte qui servaient à dessiner les interfaces graphiques des logiciels en ligne de commande.

---
<code class="nowrap" aria-hidden="true">
╭─╴╶┬╴╭─╴╶┬╴┌─╴╭─╮╭╮╷╶┬╴  
╰─╮ │ ╰─╮ │ ├─╴│ ││││ │   
╶─╯╶┴╴╶─╯╶┴╴╵  ╰─╯╵╰╯ ╵   
</code>

La *Sisifont* est un ensemble de caractères en *ANSI art* (ANSI est un encodage qui comprend beaucoup plus de caractères que l'ASCII). Ce n'est pas une police de caractère dans le sens où elle se compose avec les caractères d'une quelconque police à chasse fixe (*monospace*) tant qu'elle dispose des [caractères de boîte](https://en.wikipedia.org/wiki/Box-drawing_character).
Chaque lettre se compose en 3 caractères de large et 5 caractères de haut.

Cette typo à été assemblée à l'occasion de [Sísifo](https;//sisifo.site/).

Caractères utilisés :

<code class="nowrap inverted" aria-hidden="true">
 ╷             
 │ ╭ ╮ ┌ ┬ ┐   
 ╵ ╰ ╯ ├ ┼ ┤   
 ╶ ─ ╴ └ ┴ ┘   
</code>

<code class="nowrap" aria-hidden="true">
                                                       
  ╷     ││    ┼┼   ╭┼╴    ○    ╭╮     │     ╭╯   ╰╮    
  ╵          ┌┼┘   ╰┼╮   ╭─╯   ├┬╭          │     │    
  ╵          ┼┼    ╶┼╯    ○    ╰┴╯          ╰╮   ╭╯    
                                                       
                                                       
 ┬┴┬                             /   ╭─╮   ╶╮    ╶─╮   
       ╶┼╴         ╶─╴          /    │ │    │    ╭─╯   
              ╯           ·    /     ╰─╯   ╶┴╴   ╰─╴   
                                                       
                                                       
 ╶─╮   ╷     ┌─╴   ╭─╴   ╶─┐   ╭─╮   ╭─╮               
 ╶─┤   └┼╴   └─╮   ├─╮    ╶┤   ├─┤   ╰─┤    ·     ·    
 ╶─╯    ╵    ╶─╯   ╰─╯     ╵   ╰─╯   ╶─╯    ·     ╯    
                                                       
                                                       
                   ╶─╮   ╭─╮   ╭─┐   ┌─╮   ╭─╴   ┌─╮   
  /    ╶─╴    \    ╶─╯   │╭┤   ├─┤   │╶┤   │     │ │   
  \    ╶─╴    /    ╵     ╰╰╯   ╵ ╵   └─╯   ╰─╴   └─╯   
                                                       
                                                       
 ┌─╴   ┌─╴   ╭─╮   ╷ ╷   ╶┬╴     ╷   ╷ ╭   ╷     ╭╮╮   
 ├─╴   ├─╴   │╶╮   ├─┤    │      │   ├┴╮   │     │││   
 ╰─╴   ╵     ╰─╯   ╵ ╵   ╶┴╴   ╰─╯   ╵ ╵   ╰─╴   ╵╵╵   
                                                       
                                                       
 ╭╮╷   ╭─╮   ┌─╮   ╭─╮   ┌─╮   ╭─╴   ╶┬╴   ╷ ╷   ╷ ╷   
 │││   │ │   ├─╯   │ │   ├┬╯   ╰─╮    │    │ │   │╭╯   
 ╵╰╯   ╰─╯   ╵     ╰┬╯   ╵ ╰   ╶─╯    ╵    ╰─╯   ╰╯    
                                                       
                                                       
 ╷╷╷   ╷ ╷   ╷ ╷   ╶─╮    ┌╴   \     ╶┐     ^          
 │││   ╭─╯   ╰─┤    ─     │     \     │                
 ╰╯╯   ╵ ╵   ╶─╯   ╰─╴    └╴     \   ╶┘          ───   
                                                       
                                                       
  \          ╷             ╷          ╭╴         ╷     
       ╶─╮   ├─╮   ╭─╴   ╭─┤   ╭─╮   ╶├╴   ╭─┐   ├─╮   
       ╰─╯   ╰─╯   ╰─╴   ╰─╯   ╰─╴    ╵    ╰─┤   ╵ ╵   
                                           ╶─╯         
                                                       
  ╷     ╷    ╷     ╶┐                                  
 ╶┐    ╶┐    ├┴╮    │    ╭╮╮   ╭╮╷   ╭─╮   ╭─┐   ┌─╮   
 ╶┴╴    │    ╵ ╵    ╰╴   ╵╵╵   ╵╰╯   ╰─╯   ├─╯   ╰─┤   
       ╶╯                                  ╵       ╵   
                                                       
              ╷                                        
 ╷╭╴   ╭─╴   ╶├╴   ╷ ╷   ╷ ╷   ╷╷╷   ╮╷╭   ╷ ╷   ╶─╮   
 ╵     ╶─╯    ╰╴   ╰─╯   ╰╯    ╰╯╯   ╯╵╰   ╰─┤   ╰─╴   
                                           ╶─╯         
                                                          
  ╭╯    │    ╰╮                                           
 ╶┤     │     ├╴    ◠◡                                    
  ╰╮    │    ╭╯                                           
                                                          
                                                          
                                                          
                                                          
                                                          
                                                          
                                                          
                                                          
                                                          
                                                          
                                                        
                                                       
                                                       
                                                       
                                                       
                                                       
                                                 ╭─╮   
              ╭╮    ╷    ╷ ╷    ╷    ╭─╮   · ·   │╭│   
  ╵    ╭┼╴    ┼╴   ╶○╴   ┴┬┴    ╵    ├─╮         │╰│   
  │    ╰┼╴   ╶╯─    ╵    ─┼─    ╷    ╰─┤         ╰─╯   
  ╵                             ╵    ╰─╯               
                         ╭─╮   ╶─╴    ○          ╶╮    
 ╶╮                      │╭│                     ╭╯    
 ╰╯     //   ──┐         │╵│               ╶┼╴   ╰╴    
        \\\\               ╰─╯               ╶─╴         
                                                       
 ╶╮                                   ╮    ╭╮          
  ┤     ╯          ╭┬┬                │    ││          
 ╶╯          ╷ ╷   ╰┤│    ·           ┴    ╰╯    \\\\    
             ├─┤    ││          ╯                //    
             ╵                                         
                          \     /     ^     ~    · ·   
 ┌┬┐   ┌─┐   ┌─┐         ╭─┐   ╭─┐   ╭─┐   ╭─┐   ╭─┐   
 ├┘┤   ├─┤   │┌┤     ╵   ├─┤   ├─┤   ├─┤   ├─┤   ├─┤   
 └┴┘   └┴┘   └┴┘   ╭─╴   ╵ ╵   ╵ ╵   ╵ ╵   ╵ ╵   ╵ ╵   
                   ╰─╴                                 
  ○                 \     /     ^    · ·    \     /    
 ╭─┐   ╭┬╴   ╭─╴   ┌─╴   ┌─╴   ┌─╴   ┌─╴   ╶┬╴   ╶┬╴   
 ├─┤   ├┼╴   │     ├─╴   ├─╴   ├─╴   ├─╴    │     │    
 ╵ ╵   ╵╰╴   ╰┬╴   ╰─╴   ╰─╴   ╰─╴   ╰─╴   ╶┴╴   ╶┴╴   
              ╯                                        
  ^    · ·          ~     \     /     ^     ~    · ·   
 ╶┬╴   ╶┬╴   ┌─╮   ╭╮╷   ╭─╮   ╭─╮   ╭─╮   ╭─╮   ╭─╮   
  │     │    ┼╴│   │││   │ │   │ │   │ │   │ │   │ │   
 ╶┴╴   ╶┴╴   └─╯   ╵╰╯   ╰─╯   ╰─╯   ╰─╯   ╰─╯   ╰─╯   
                                                       
              \     /     ^    · ·    /                
       ╭─/   ╷ ╷   ╷ ╷   ╷ ╷   ╷ ╷   ╷ ╷   ├─╮   ┌─╮   
 \ /   │/│   │ │   │ │   │ │   │ │   ╰─┤   │ │   │╶┤   
 / \   /─╯   ╰─╯   ╰─╯   ╰─╯   ╰─╯   ╶─╯   ├─╯   ╵╰╯   
                                                       
                                                       
  \     /     ^     ~    · ·    ○                 \    
 ╶─╮   ╶─╮   ╶─╮   ╶─╮   ╶─╮   ╶─╮   ╶┬╮   ╭─╴   ╭─╮   
 ╰─╯   ╰─╯   ╰─╯   ╰─╯   ╰─╯   ╰─╯   ╰┴╴   ╰┬╴   ╰─╴   
                                            ╯          
                                                       
  /     ^    · ·    \     /     ^    · ·    ╶┤    ~    
 ╭─╮   ╭─╮   ╭─╮   ╶┐    ╶┐    ╶┐    ╶┐    ╭─┤   ╭╮╷   
 ╰─╴   ╰─╴   ╰─╴   ╶┴╴   ╶┴╴   ╶┴╴   ╶┴╴   ╰─╯   ╵╰╯   
                                                       
                                                       
  \     /     ^     ~    · ·    ·           \     /    
 ╭─╮   ╭─╮   ╭─╮   ╭─╮   ╭─╮   ╶─╴   ╭─/   ╷ ╷   ╷ ╷   
 ╰─╯   ╰─╯   ╰─╯   ╰─╯   ╰─╯    ·    /─╯   ╰─╯   ╰─╯   
                                                       
                               
  ^    · ·    /          · ·   
 ╷ ╷   ╷ ╷   ╷ ╷   ├─╮   ╷ ╷   
 ╰─╯   ╰─╯   ╰─┤   ├─╯   ╰─┤   
             ╶─╯         ╶─╯   
</code>
