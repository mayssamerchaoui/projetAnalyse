# projetAnalyse


<p> <strong><h2>Introduction général </h2></strong> </p>
En analyse numérique, il existe une vaste famille d’algorithmes dont le but principal est d’estimer la valeur numérique de l’intégrale définie sur un domaine particulier pour une fonction donnée (par exemple l’intégrale d’une fonction d’une variable sur un intervalle). voila des exemple que le calcule simple d integrale est impossible

<p> <strong> <h2>But </h2></strong> </p>
Ce projet permet d'étuder une fonction f(x) et de représenter graphiquement les méthodes d'intégration numériques , comme (méthode de rectangle , méthode des trapézes , méthode des points milieux , méthodes de simspon) en donnant pour chaque fonction sa valeur approché ,valeur exacte et l'erreur.

<strong> <p><h2>Méthodes d'intégration numérique</h2></strong> </p>

Si f est une fonction continue sur un intervalle [a,b], bien souvent on ne sait pas calculer une primitive de f. Ainsi, si l'on désire obtenir la valeur de <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/4.png" /> , il faut parfois se contenter d'obtenir une valeur approchée à l'aide d'une méthode d'intégration numérique.
  La plupart des méthodes d'intégration numérique fonctionnent sur le même principe. On commence par couper le gros intervalle [a,b] en N plus petits intervalles [ai,ai+1], avec a1=a et aN+1=b. Puis, pour chaque intervalle [ai,ai+1], on essaie d'approcher <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/5.png" />. Les moyens les plus simples sont :
<ol>
<li><p> <strong>Méthode des Rectangles à gauche :</strong> </p></li>
  
Considérons donc une fonction de R dans R continue sur un intervalle [a,b]. Pour un physicien, intégrer signifie la plupart du temps calculer l'aire sous la courbe de la fonction entre a et b. La première méthode qui vienne à l'esprit, c'est de découper l'aire entre la courbe f(x), l'axe des x et les droites x= a et x = b, en une multitude de petits rectangles. Découpons l'intervalle [a,b] en rectangles élémentaires de largeur h, h étant petit. Le rectangle n° i aura donc pour longueur f(a + i*h). Sa surface est donc égale à h*f(a + i*h). L'aire sous la courbe entre a et b est obtenue en sommant tous ces petits rectangles. Reste qu'en posant cette relation, j'ai fait l'hypothèse implicite que la courbe limite le coté gauche de mon rectangle. On peut imaginer d'autres découpages.

<p>on approche  <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/1.png" />
 par  <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/2.png" /> . 
 Géométriquement, cela signifie qu'on approche l'intégrale de f par l'aire des rectangles hachurés en vert :<br />
  
  
 <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/3.png" /></p> </p>



<li><p> <strong>Méthode du Trapèse :</strong> </p></li>
C’est la méthode la plus simple qui consiste à interpoler la fonction f à intégrer par une fonction constante (polynôme de degré 0).

Si ξ est le point d’interpolation, la formule est la suivante :<br/>
<img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/19.PNG" />

Le choix de ξ influence l’erreur E(f) = I – I(f) :
<ul>
    <li> Si ξ = a ou ξ = b, l’erreur est donnée par:</li>
  </ul>
<img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/17.PNG" />
C’est la méthode du rectangle qui est d’ordre 0.
      Si ξ = (a + b)/2, l’erreur est donnée par
<img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/18.PNG" />

Il s’agit de la méthode du point milieu qui est d’ordre 1.
Ainsi, le choix du point milieu améliore l’ordre de la méthode : celle du rectangle est exacte (c’est-à-dire E(f) = 0) pour les fonctions constantes alors que celle du point milieu est exacte pour les polynômes de degré 1. Ceci s’explique par le fait que l’écart d’intégration de la méthode du point milieu donne lieu à deux erreurs d’évaluation, de valeurs absolues égales et de signes opposés.

<p>on approche<img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/6.png" />
par 
<img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/7.png" /> .
Géométriquement, cela signifie qu'on approche l'intégrale de f par l'aire des trapèzes hachurés en marron :<br />
<img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/8.png" /></p> </p>

<li><p> <strong>la méthode du point milieu: <p> </strong></li>
<p>  on approche <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/9.png" />
par <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/10.png" />
Géométriquement, cela signifie qu'on approche l'intégrale de f par l'aire des rectangles hachurés en bleu :<br />
  <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/11.png" /></p> </p>
  
  <li><p> <strong>La méthode de Simpson :</p> </strong> </li>
  
 En interpolant f par un polynôme de degré 2 (3 degrés de liberté), 3 points (ou conditions) sont nécessaires pour le caractériser : les valeurs aux extrémités a, b, et celle choisie en leur milieu m = (a + b) / 2. La méthode de Simpson est basée sur un polynôme de degré 2 (intégrale d’une parabole), tout en restant exacte pour des polynômes de degré 3 ; elle est donc d’ordre 3 :
<img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/20.PNG" />

L’erreur globale est donnée par
<img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/21.PNG" />
Remarque : comme la méthode du point milieu qui caractérise un polynôme de degré 0 et qui reste exacte pour tout polynôme de degré 1, la méthode de Simpson caractérise un polynôme de degré 2 et reste exacte pour tout polynôme de degré 3. Il s’agit d’une sorte d’anomalie où se produisent des compensations bénéfiques à l’ordre de la méthode.
<p> on approche <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/15.PNG" />
par  <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/16.PNG" /></p> </p>
Géométriquement,La courbe rouge représente le polynôme d'approximation P(x):<br />
<img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/14.PNG" /> 

</ol>

