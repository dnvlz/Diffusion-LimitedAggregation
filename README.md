# Diffusion-LimitedAggregation
Diffusion-limited aggregation (DLA) is the process whereby particles undergoing a random walk due to Brownian motion cluster together to form aggregates.

There are various versions of DLA, but the one we study is as follows. We start with a square grid and a single particle in the middle. The particle performs a random walk from square to square on the grid until it reaches a point on the edge of the system, at which point it "sticks" to the edge, becoming anchored there and immovable. Then a second particle starts at the center and does a random walk until it sticks either to an edge or to the other particle. Then a third particle starts, and so on.

a) Using *vpython*, we [animate](https://drive.google.com/file/d/1-hU4MiXmSjXytoFnIC9sUsQIGjeq3eju/view?usp=sharing) the DLA process on a 101×101 lattice—we choose an odd length for the side of the square so that there is one lattice site exactly in the center. Then, we repeatedly introduce a new particle at the center and have it walk randomly until it sticks to an edge or an anchored particle.

b) In the interests of speed, the [animation](https://drive.google.com/file/d/1-j7fUBAw6FAeLStQL08aJrK3bGGxXbBX/view?usp=sharing) is modified to show only the anchored particles on the screen and not the randomly walking ones. The program stops running once there is an anchored particle in the center of the grid, at the point where each particle starts its random walk.
______________________________________________________________________________________________________________________
La agregación limitada por difusión (ALD) es el proceso mediante el cual las partículas que experimentan una caminata aleatoria debido al movimiento browniano se agrupan para formar agregadoS.

Hay varias versiones de la ALD, pero la que estudiamos es la siguiente. Comenzamos con una cuadrícula cuadrada y una sola partícula en el medio. La partícula realiza una caminata aleatoria de un cuadrado a otro hasta que llega a un punto en el borde del sistema, ancladándose a él. Luego, una segunda partícula comienza en el centro y realiza un recorrido aleatorio hasta que se pega a un borde o a otra partícula. Luego comienza una tercera partícula, y así sucesivamente.

a) Usando *vpython*, [animamos](https://drive.google.com/file/d/1-hU4MiXmSjXytoFnIC9sUsQIGjeq3eju/view?usp=sharing) el proceso de la ALD en una red de 101×101: elegimos una longitud impar para los lados del cuadrado, asegurando que haya un sitio de la red exactamente en el centro. Luego, introducimos repetidamente una nueva partícula en el centro y hacemos que camine aleatoriamente hasta que se adhiera a un borde o una partícula anclada.

b) En aras de la velocidad, la [animación](https://drive.google.com/file/d/1-j7fUBAw6FAeLStQL08aJrK3bGGxXbBX/view?usp=sharing) se modifica para mostrar sólo las partículas ancladas en la pantalla y no su recorrido total. El programa deja de ejecutarse una vez que hay una partícula anclada en el centro de la cuadrícula, en el punto donde cada partícula comienza su recorrido aleatorio.
