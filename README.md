# Diffusion-LimitedAggregation
Diffusion-limited aggregation (DLA) is the process whereby particles undergoing a random walk due to Brownian motion cluster together to form aggregates of such particles.

There are various versions of DLA, but the one we’ll study is as follows. We start with a square grid and a single particle in the middle. The particle performs a random walk from square to square on the grid until it reaches a point on the edge of the system, at which point it “sticks” to the edge, becoming anchored there and immovable. Then a second particle starts at the center and does a random walk until it sticks either to an edge or to the other particle. Then a third particle starts, and so on. Each particle starts at the center and walks until it sticks either to an edge or to any anchored particle.

a) We simulate the DLA process on a 101×101 lattice—we choose an odd length for the side of the square so that there is one lattice site exactly in the center. Then, we repeatedly introduce a new particle at the center and have it walk randomly until it sticks to an edge or an anchored particle.

b) In the interests of speed, the program is modified to show only the anchored particles on the screen and not the randomly walking ones. The program stops running once there is an anchored particle in the center of the grid, at the point where each particle starts its random walk. Once there is a particle at this point, there’s no point running any longer because any further particles added will
be anchored the moment they start out.
