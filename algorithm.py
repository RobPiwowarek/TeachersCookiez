import itertools
import logging

import selection
import crossover
from generate import *


class Algorithm:
    base_mutation_chance = 35
    punishment_factor = 11

    def __init__(self, crossover_method, breeding_method, mutation_method, selection_method):
        self.crossover = crossover_method
        self.mutation = mutation_method
        self.selection = selection_method
        self.breeding = breeding_method

    def calculate_genetic(self, test_results, max_generations=100000, mutation_chance=20, population_count=64,
                          elitism_factor=0.25):
        k = int(population_count * elitism_factor)

        base_population = []
        for x in range(population_count):
            base_population.append(generate_cookiez_for_test_results(test_results))

        optimal_cookiez_distribution = self.calculate_optimal_for_test_results(test_results)
        optimal_children = list(map(lambda child_attribs: Child(child_attribs[0], child_attribs[1]),
                                    zip(test_results, optimal_cookiez_distribution)))
        optimal_fitness = self.get_fitness(optimal_children)
        #
        generation_counter = 0
        population = base_population
        best_children = []
        best_fitness = -1

        while generation_counter < max_generations:
            # best in population
            best_children = self.select_k_best(population, 1)[0]
            best_fitness = self.get_fitness(best_children)
            logging.info("gen: %d best fitness: %d", generation_counter, best_fitness)
            # stop criterion
            if best_fitness == optimal_fitness:
                break

            # selection
            chosen_ones = self.selection(self, population, k)

            # crossover
            breed_ones = self.breeding(self, chosen_ones, population_count - k)
            # mutation
            breed_ones = self.mutate_population(breed_ones, mutation_chance)

            # new population
            population = list(chosen_ones) + list(breed_ones)
            generation_counter += 1

        logging.info("finished at generation: %d", generation_counter)
        logging.info("fitness: %d", best_fitness)
        logging.info("optimal fitness: %d", optimal_fitness)
        logging.info("test results: %s", test_results)
        logging.info("best cookie assignment: %s", [child.cookiez for child in best_children])

        return best_children, best_fitness, generation_counter

    @staticmethod
    def calculate_optimal(children):
        current_cookie = 1

        i = 0
        while i < len(children):
            children[i].cookiez = max(current_cookie, children[i].cookiez)

            if i == len(children) - 1:
                break

            if children[i].testResult < children[i + 1].testResult:
                current_cookie = current_cookie + 1
            else:
                current_cookie = 1

            i = i + 1

        current_cookie = 1

        i = len(children) - 1
        while i >= 0:
            children[i].cookiez = max(current_cookie, children[i].cookiez)

            if i == 0:
                break

            if children[i].testResult < children[i - 1].testResult:
                current_cookie += 1
            else:
                current_cookie = 1

            i = i - 1

        return children

    def calculate_optimal_for_test_results(self, test_results):
        children = list(map(lambda result: Child(result), test_results))
        optimal = self.calculate_optimal(children)
        optimal = list(map(lambda child: child.cookiez, optimal))
        return optimal

    def print_optimal(self, children):
        result = self.calculate_optimal(children)

        for pos, child in enumerate(result):
            print("pos: " + str(pos) + " cookiez: " + str(child.cookiez) + " test result: " + str(
                child.testResult) + "\n")

    @staticmethod
    def add_or_remove_cookie(cookies):
        if random.randint(0, 1) == 1:
            return cookies - 1
        else:
            return cookies + 1

    def mutate(self, children, chance):
        for child in children:
            rolled_value = random.randint(0, 100)
            if rolled_value <= chance:
                child.cookiez = self.add_or_remove_cookie(child.cookiez)

        return children

    def mutate_with_decreasing_chance(self, children, chance):
        chance2 = chance
        for child in children:
            rolled_value = random.randint(0, 100)
            if rolled_value <= chance2:
                child.cookiez = self.add_or_remove_cookie(child.cookiez)
                chance2 = chance2 / 2

    # mutation is a function
    def mutate_population(self, population, chance=base_mutation_chance):
        mutated = list(map(lambda children: self.mutation(self, children, chance), population))
        return mutated

    def get_fitness(self, children):
        cookie_sum = sum(abs(child.cookiez) for child in children)
        bad_pos_count = 0
        for i in range(1, len(children)):
            child1 = children[i - 1]
            child2 = children[i]
            if child1.testResult < child2.testResult:
                if child1.cookiez >= child2.cookiez:
                    bad_pos_count += 1
            elif child1.testResult > child2.testResult:
                if child1.cookiez <= child2.cookiez:
                    bad_pos_count += 1
            if child1.cookiez < 1:
                bad_pos_count += 1  # double punishment for < 1 cookies
        if children[-1].cookiez < 1:
            bad_pos_count += 1

        return cookie_sum + bad_pos_count * self.punishment_factor

    def all_with_all_breeding(self, population, how_many_children = None):
        for pair in itertools.combinations(population, 2):
            yield self.crossover(self, pair[0], pair[1])

    def random_breeding(self, population, how_many_children):
        for i in range(how_many_children):
            random_pair = random.choices(population, k=2)
            yield self.crossover(self, random_pair[0], random_pair[1])

    def select_k_best(self, population, k):
        return selection.k_best(population, k, self.get_fitness)

    def select_weighted(self, population, k):
        return selection.weighted(population, k, self.get_fitness)

    def equal_crossover(self, genome1, genome2):
        return crossover.equal(genome1, genome2)
