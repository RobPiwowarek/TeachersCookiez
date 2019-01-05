from algorithm import Algorithm
from crossover import *
from generate import *
from datetime import datetime

# stop iterating at max generations or at being in the optimal
max_generations = 100000
mutation_chance = 20
population_count = 64
children_count = 50
elitism_factor = 0.25

k = int(population_count * elitism_factor)
algo = Algorithm()
test_results = generate_tests_results_only(children_count)



# time start
tstart = datetime.now()

base_population = []
for x in range(population_count):
    base_population.append(generate_cookiez_for_test_results(test_results))

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
    breed_ones = algo.mutate_population(breed_ones, algo.mutate, mutation_chance)

    # new population
    population = list(chosen_ones) + list(breed_ones)

    generation_counter += 1

if generation_counter >= max_generations:
    best_children = population[0]

# time end
tend = datetime.now()

print("generation counter = " + str(generation_counter))
print("fitness: " + str(algo.get_fitness(best_children)))
print("optimal fitness: " + str(algo.get_fitness(optimal_children)))

print("cookiez : results")
for child in best_children:
    print(str(child.cookiez) + " : " + str(child.testResult))

print(str(tend - tstart))