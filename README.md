# projetAnalyse

<p> <strong>Introduction général</strong> </p>
En analyse numérique, il existe une vaste famille d’algorithmes dont le but principal est d’estimer la valeur numérique de l’intégrale définie sur un domaine particulier pour une fonction donnée (par exemple l’intégrale d’une fonction d’une variable sur un intervalle). voila des exemple que le calcule simple d integrale est impossible

<p> <strong> But </strong> </p>
Ce projet permet d'étuder une fonction f(x) et de représenter graphiquement les méthodes d'intégration numériques , comme (méthode de rectangle , méthode des trapézes , méthode des points milieux , méthodes de simspon) en donnant pour chaque fonction sa valeur approché ,valeur exacte et l'erreur.

<strong> <p>Méthodes d'intégration numérique</strong> </p>

Si f est une fonction continue sur un intervalle [a,b], bien souvent on ne sait pas calculer une primitive de f. Ainsi, si l'on désire obtenir la valeur de , il faut parfois se contenter d'obtenir une valeur approchée à l'aide d'une méthode d'intégration numérique.
  La plupart des méthodes d'intégration numérique fonctionnent sur le même principe. On commence par couper le gros intervalle [a,b] en N plus petits intervalles [ai,ai+1], avec a1=a et aN+1=b. Puis, pour chaque intervalle [ai,ai+1], on essaie d'approcher . Les moyens les plus simples sont :

<p> <strong>Méthode des Rectangles à gauche</strong> </p>
<p>on approche  <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/1.png" />
 par  <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/2.png" /> . 
 Géométriquement, cela signifie qu'on approche l'intégrale de f par l'aire des rectangles hachurés en vert :<br />
  
  
 <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/3.png" /></p>


<p> <strong>Méthode du Trapèse</strong> </p>

On considère une fonction $f(x)$ définie sur un intervalle $[a,b]$ , et dont on veut calculer l’intégrale $ ∫ f(x) dx$ sur ce même intervalle. La méthode des trapèzes consiste à diviser l’intervalle $[a,b]$ en une série d’intervalles $[x_i-_1,x_i]$ , à remplacer la courbe $y = f(x)$ par un segment de droite, et à calculer l’aire du trapèze ainsi obtenu.

<p> <strong>Méthode du Simpson</strong> </p>
En général, pour appliquer cette méthode d'intégration, on découpe l'intervalle [a,b] en n intervalles de longueur (b−a)/n ( b − a ) / n , et on applique la formule précédente sur chacun des sous-intervalles. On a alors, en posant h=b−an h = b − a n : ∫baf(t)dt≃h6n−1∑k=0(f(a+kh)+4f(a+(k+1/2)h)+f(a+(k+1)h))


