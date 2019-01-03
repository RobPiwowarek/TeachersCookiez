from algorithm import Algorithm
from child import Child
from generate import *
import selection
import crossover


algo = Algorithm()

population_count = 50
children_count = 50

test_results = generate_tests_results_only(children_count)

optimal_cookiez_distribution = algo.calculate_optimal()

base_population = []
for x in range(population_count):
    base_population.append(generate_cookiez_for_test_results(test_results))

# stop iterating at max generations or at being in the optimal
max_generations = 1000





