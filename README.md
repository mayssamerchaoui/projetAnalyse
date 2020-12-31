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

<p>on approche  <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/1.png" />
 par  <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/2.png" /> . 
 Géométriquement, cela signifie qu'on approche l'intégrale de f par l'aire des rectangles hachurés en vert :<br />
  
  
 <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/3.png" /></p> </p>



<li><p> <strong>Méthode du Trapèse :</strong> </p></li>

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
<p> on approche <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/15.PNG" />
par  <img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/16.PNG" /></p> </p>
Géométriquement,La courbe rouge représente le polynôme d'approximation P(x):<br />
<img src= "https://github.com/mayssamerchaoui/projetAnalyse/blob/main/14.PNG" /> 

</ol>

