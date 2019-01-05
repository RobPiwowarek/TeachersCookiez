from algorithm import Algorithm
from crossover import *
from generate import *

algo = Algorithm()

#

population_count = 50
children_count = 50
k = population_count // 2

#

test_results = generate_tests_results_only(children_count)

#

base_population = []
for x in range(population_count):
    base_population.append(generate_cookiez_for_test_results(test_results))

# stop iterating at max generations or at being in the optimal
max_generations = 1000

optimal_cookiez_distribution = algo.calculate_optimal_for_test_results(test_results)

optimal_children = list(map(lambda tuple: Child(tuple[0], tuple[1]), zip(test_results, optimal_cookiez_distribution)))

#


generation_counter = 0
population = base_population
while generation_counter < max_generations:

    # selection
    chosen_ones = algo.select_k_best(population, k)

    print("gen: " + str(generation_counter) + " fitness: " + str(algo.get_fitness(chosen_ones[0])))
    # evaluation & stop cryterium TODO: save result
    if algo.get_fitness(chosen_ones[0]) == algo.get_fitness(optimal_children):
        best_children = chosen_ones[0]
        break

    # crossover
    breed_ones = algo.random_breeding(chosen_ones, population_count - k, equal)
    # mutation
    breed_ones = algo.mutate_population(breed_ones, algo.mutate)

    # new population

    population = list(chosen_ones) + list(breed_ones)

    generation_counter += 1

if generation_counter >= max_generations:
    best_children = population[0]

print("generation counter = " + str(generation_counter))
print("fitness: " + str(algo.get_fitness(best_children)))
print("optimal fitness: " + str(algo.get_fitness(optimal_children)))

print("cookiez : results")
for child in best_children:
    print(str(child.cookiez) + " : " + str(child.testResult))