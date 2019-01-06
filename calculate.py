from datetime import datetime
from algorithm import Algorithm
import sys
from generate import *
import logging

def calculate_times_for_ranges(children_count_range, mutation_range, population_range, elitism_range):
    logging.basicConfig(filename="cookies-%s.log" % datetime.now(), level=logging.DEBUG)
    print("children;mutation_chance;population_count;elitism_factor;generations_at_end;best_fitness;time")
    for chld_cnt in children_count_range:
        for mut_chnc in mutation_range:
            for pop_cnt in population_range:
                for elitism in elitism_range:
                    max_gen = 20000
                    starttime = datetime.now()
                    best_children, best_fitness, generation = calculate(chld_cnt, max_gen, mut_chnc, pop_cnt, elitism)
                    endtime = datetime.now()
                    print("%d;%d;%d;%d;%d;%d;%s" % (chld_cnt, mut_chnc, pop_cnt, elitism, generation, best_fitness, endtime - starttime))

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
