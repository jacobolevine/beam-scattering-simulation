# beam-scattering-simulation

Classical Beam Scattering Simulation in a Screened Central Potential

Overview

This project simulates the scattering of a particle beam interacting with a central force in two dimensions. The goal is to study how the range of the interaction affects particle trajectories, scattering angles, and detector distributions.

Particles are initialized as a beam entering from the left and evolve under a Yukawa-type (screened) central force, which introduces a finite interaction range. The simulation numerically integrates the equations of motion and analyzes the resulting scattering behavior.

Physics Model

Each particle moves under a central force derived from the screened potential:

V(r) = (k / r) * exp(-r / a)

The resulting force magnitude is:

F(r) = k * exp(-r / a) * (1 / r^2 + 1 / (a r))

The force components are:

Fx = F(r) * (x / r)
Fy = F(r) * (y / r)

To avoid numerical instability near r = 0, a small softening parameter is introduced:

r = sqrt(x^2 + y^2 + eps^2)

Simulation Setup

Particles start at x = -L. Their initial vertical positions y0 are sampled from a Gaussian distribution centered at 0. The initial velocity is vx = v0 and vy = 0. The motion is integrated step-by-step in time until the particle exits the region between -L and L.

Outputs

For each value of the interaction range parameter a, the simulation produces several outputs. A trajectory plot shows the paths of particles as they pass through the interaction region. A scattering angle histogram shows the distribution of final angles, computed as theta = atan2(vy, vx). A detector histogram shows the distribution of particle positions when they reach x = L, representing where they would land on a detector. A summary plot shows the mean absolute scattering angle as a function of a.

Key Findings

As the interaction range parameter a increases, particles experience stronger deflection over a larger region of space. This leads to broader distributions of scattering angles and wider spreads in detector hit positions. When a is small, the interaction is short-range and only particles that pass close to the origin are strongly deflected. This demonstrates how introducing a finite interaction range qualitatively changes scattering behavior.

Numerical Details

The simulation uses a time step of dt = 0.005 and a softening parameter eps = 0.05. Approximately 200 particles are simulated in each run. The system is modeled in dimensionless units with m = 1 and k = 1, so results reflect relative behavior rather than a specific physical system.

Project Structure

The function simulate(...) integrates the motion of a single particle. The function run(...) executes the simulation across a beam of particles. The main script generates the initial beam, runs the simulation for different values of a, and produces plots of trajectories and distributions.

Possible Extensions

This simulation can be extended by comparing with an unscreened inverse-square force, introducing velocity spread in the beam, extending the model to three dimensions, adding multiple scattering centers, or implementing higher-order numerical integration methods.

Summary

This project models classical beam scattering under a central force with finite range. It demonstrates how interaction range affects trajectories and observable distributions, and provides a computational introduction to ideas that extend naturally to scattering theory in physics.