from algorithm import Algorithm
from child import Child
from generate import *
from selection import *
from crossover import *

algo = Algorithm()

#

population_count = 50
children_count = 50
k = population_count / 2

#

test_results = generate_tests_results_only(children_count)

#

base_population = []
for x in range(population_count):
    base_population.append(generate_cookiez_for_test_results(test_results))

# stop iterating at max generations or at being in the optimal
max_generations = 1000

optimal_cookiez_distribution = algo.calculate_optimal_for_test_results(test_results)

#


generation_counter = 0
population = base_population
while generation_counter < max_generations:

    # selection
    chosen_ones = algo.select_k_best(population, k)

    # evaluation & stop cryterium TODO: save result
    cookie_distribution = list(map(lambda child: child.cookiez, chosen_ones[0]))
    if cookie_distribution == optimal_cookiez_distribution:
        break

    # crossover
    breed_ones = algo.random_breeding(chosen_ones, population_count - k, equal)

    # new population

    population = list(chosen_ones) + list(breed_ones)

    # mutation
    algo.mutate_population(population, algo.mutate)

    generation_counter += 1
