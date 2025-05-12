import numpy as np
from math import pow

def generateDistances(n_cities):
  cities = np.random.randint(3,51, size=(n_cities,n_cities))
  cities = (cities + cities.T)//2
  np.fill_diagonal(cities, 0)
  return cities
def generatePheromones(n_cities):
  pheromones = np.ones((n_cities,n_cities), dtype=float)
  return pheromones

def update_pheromone(n_ants, visited_cities, cities,pheromones):
  #visited_cities was appended with the order of visiting so now we have a full path
  pher = np.ones_like(pheromones, dtype=float)
  for i in range(n_ants):
    for j in range(len(visited_cities)-1):
      pher[visited_cities[j]][visited_cities[j+1]] += 2/cities[visited_cities[j]][visited_cities[j+1]]
      pher[visited_cities[j+1]][visited_cities[j]] += 2/cities[visited_cities[j+1]][visited_cities[j]]

  for i in range(len(visited_cities)):
    for j in range(len(visited_cities)):
      pheromones[i][j] = (0.6)*pheromones[i][j] + pher[i][j]
  return pheromones


def calc_probability(current_city, cities, pheromones, visited_cities, j):
  prob = 0.0
  z=0
  for i in range(cities.shape[0]):
    if i not in visited_cities:
      if i != current_city:
        z += (pheromones[current_city][i])*(1/(cities[current_city][i]))
  if j not in visited_cities:
    if z != 0.0:
      prob = (pheromones[current_city][j]) * (pow(1 / (cities[current_city][j]), 2)) / (z)
    else:
      prob = 0.0
  else:
    prob = 0.0
  # for i in range(cities.shape[0]):
  #   if z != 0.0:
  #     if i != current_city:
  #       prob[i] = (pheromones[current_city][i])*(pow(1/(cities[current_city][i]),2)) / (z)
  #     else:
  #       prob[i] = 0.0
  return prob

def move(current_city, cities, pheromones, visited_cities):
  min_cost = 0
  max_prob = 0
  next_city = -1
  for i in range(cities.shape[1]):
    prob = calc_probability(current_city, cities, pheromones, visited_cities,i)
    if prob >= max_prob:
      max_prob = prob
      if i not in visited_cities:
        next_city = i
      # next_city = i if i not in visited_cities
    #calc th ecost using the formula
      path_cost = cities[current_city][i]
    if min_cost == 0:
      min_cost = path_cost
    else:
      if path_cost < min_cost:
        min_cost = path_cost
  print(f"next city: {next_city}")
  print(f"max prob: {max_prob}")
  return next_city, min_cost

def start_end(cities, n_ant, pheromones):
  n_cities = len(cities)
  visited_cities=[]
  visited_cities.append(0)
  current_city= 0
  total_cost = 0
  i=0
  while len(visited_cities) < n_cities:
    print(i)
    i+=1
    next_city, cost = move(current_city, cities, pheromones, visited_cities)
    total_cost += cost
    visited_cities.append(next_city)
    current_city = next_city
# must return to the starting point
  total_cost += cities[current_city][0]
  return visited_cities, total_cost

def run_AOC(n_cities, n_ant):
  distances = generateDistances(n_cities)
  pheromones = generatePheromones(n_cities)
  visited_cities=[]
  # visited_cities.append(0)
  min_path = 0
  optimum_path=[]
  for i in range(50): #from start to finish
    visited_cities, path_cost = start_end(distances, n_ant, pheromones)
    if min_path == 0:
      min_path = path_cost
      optimum_path = visited_cities
    else:
      if path_cost < min_path:
        min_path = path_cost
        optimum_path = visited_cities
    print(f"optimum path: {optimum_path}")
    pheromones = update_pheromone(n_ant, visited_cities,distances, pheromones)
  print(f"min path: {min_path}")
  return

run_AOC(10, 1)