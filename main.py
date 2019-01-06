from datetime import datetime
from algorithm import Algorithm
import sys
from generate import *
import logging


def calculate(children_count, max_generations, mutation_chance, population_count, elitism_factor):
    random.seed(32768)

    algo = Algorithm(breeding_method=Algorithm.random_breeding,
                     mutation_method=Algorithm.mutate,
                     crossover_method=Algorithm.equal_crossover,
                     selection_method=Algorithm.select_k_best)

    test_results = generate_tests_results_only(children_count)

    # # time start
    # tstart = datetime.now()

    return algo.calculate_genetic(test_results,
                                  max_generations,
                                  mutation_chance,
                                  population_count,
                                  1 / elitism_factor)


if __name__ == '__main__':
    # max_generations = 1000
    # mutation_chance = 20
    # population_count = 64
    # elitism_factor = 0.25
    # children_count = 50
    if len(sys.argv[1:]) < 5:
        print("Usage: ./main children_count max_generations mutation_chance population_count elitism_factor")
        sys.exit(1)

    logging.basicConfig(filename="cookies-%s.log" % datetime.now(), level=logging.DEBUG)

    children_count, max_generations, mutation_chance, population_count, elitism_factor = (int(x) for x in sys.argv[1:])

    calculate(children_count, max_generations, mutation_chance, population_count, elitism_factor)
    # # time end
    # tend = datetime.now()
    # print(str(tend - tstart))
