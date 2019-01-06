from datetime import datetime

from algorithm import Algorithm
import sys
from generate import *

if __name__ == '__main__':
    # max_generations = 1000
    # mutation_chance = 20
    # population_count = 64
    # elitism_factor = 0.25
    # children_count = 50
    children_count, max_generations, mutation_chance, population_count, elitism_factor = (int(x) for x in sys.argv[1:])

    random.seed(32768)

    algo = Algorithm(breeding_method=Algorithm.random_breeding,
                     mutation_method=Algorithm.mutate,
                     crossover_method=Algorithm.equal_crossover,
                     selection_method=Algorithm.select_k_best)

    algo.logger.setLevel("INFO")

    test_results = generate_tests_results_only(children_count)

    # time start
    tstart = datetime.now()

    calculated_children, calculated_fitness = algo.calculate_genetic(test_results,
                                                                     max_generations,
                                                                     mutation_chance,
                                                                     population_count,
                                                                     1/elitism_factor)
    # time end
    tend = datetime.now()
    print(str(tend - tstart))
