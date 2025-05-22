# Ant Colony Optimization (ACO) for Traveling Salesman Problem (TSP)

---

## Overview

This project implements the **Ant Colony Optimization (ACO)** metaheuristic algorithm to solve the classic **Traveling Salesman Problem (TSP)**. Given a set of cities and the distances between them, the algorithm finds a near-optimal shortest path that visits each city exactly once and returns to the starting point.

ACO is inspired by the foraging behavior of ants and uses a combination of **pheromone trails** and **heuristic information** to probabilistically construct solutions and iteratively improve them.

---

## Features

- Probabilistic path selection based on pheromone intensity and distance heuristic
- Pheromone update mechanism balancing exploration and exploitation
- Support for configurable number of ants and cities
- Extensible code for experimenting with ACO parameters
- Visualization-ready output of best path and cost
- Modular design to easily integrate custom distance matrices

---

## Parameters you can customize:

- Number of cities
- Number of ants
- Number of iterations
- Distance matrix (optional)

---

## How It Works

1. **Initialization:**  
   Generate initial pheromone levels and city distances.

2. **Construct Solutions:**  
   Each ant constructs a path probabilistically by choosing the next city based on pheromone strength and distance heuristic, avoiding already visited cities.

3. **Pheromone Update:**  
   After all ants complete their tours, pheromone trails are updated with evaporation and reinforcement based on the quality (cost) of the solutions.

4. **Iteration:**  
   Repeat the solution construction and pheromone update for a fixed number of iterations or until convergence.

---

## Future Work

- Add visualization of city graph and ant paths
- Experiment with different pheromone evaporation rates and heuristics
- Extend to solve other combinatorial optimization problems
- Add concurrency for ants moving simultaneously

## Contributing

Contributions and suggestions are welcome! Feel free to open issues or submit pull requests.
