import random

def k_best(population, k, get_fitness):
    sorted_population = sorted(population, key=lambda children: get_fitness(children))
    
    return sorted_population[:k]

def weighted(population, k, get_fitness):
    return random.choices(population, weights = [1/get_fitness(children) for children in population], k = k)
