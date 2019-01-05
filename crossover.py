import random
from child import Child

def base_crossover(genome1, genome2, weights):
    """
    base method, should probably not be used directly
    
    creates new genome from two parent genomes by binary selection according to weights
    genome1 and genome2 should be equal length iterables
    weights should be an iterable of length 2 with float compatible types (except decimal)
    """
    if len(genome1) != len(genome2):
        raise TypeError("Genomes must have equal length")
    
    result = []
    
    for i in range(len(genome1)):
        parent1 = genome1[i]
        parent2 = genome2[i]
        child = random.choices(population = (parent1, parent2), weights = weights, k = 1)[0] # python 3.6+
        result.append(Child(child.testResult, child.cookiez))
    
    return result

def equal(genome1, genome2):
    """
    creates new genome from two parent genomes
    each item of the result is either from genome1 or genome2, selected with equal probability
    """
    return base_crossover(genome1, genome2, None)

def proportional_to_fitness(genome1, genome2, get_fitness):
    """
    creates new genome from two parent genomes
    each item of the result is either from genome1 or genome2, selected with probability
    proportional to the genome's fitness value
    """
    
    # might want to change it to .fitness() or some other way to get the fitness?
    return base_crossover(genome1, genome2, [1/get_fitness(genome1), 1/get_fitness(genome2)])
        
def single_point(genome1, genome2):
    """
    creates new genome from two parent genomes by single-point crossover
    """
    if len(genome1) != len(genome2):
        raise TypeError("Genomes must have equal length")
    
    result = []
    
    point = random.randint(0, len(genome1)-1)
    
    for i in range(0, point):
        result.append(genome1[i])
        
    for i in range(point, len(genome1)-1):
        result.append(genome2[i])
        
    return result
    
