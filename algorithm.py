import random
import crossover
import selection
import itertools
from child import Child

class Algorithm:
    base_mutation_chance = 20
    punishment_factor = 11
    selection_size = 25
    breeding_size = 25

    def calculate_optimal(self, children):
        current_cookie = 1

        i = 0
        while i < len(children):
            children[i].cookiez = max(current_cookie, children[i].cookiez)

            if i == len(children)-1:
                break

            if children[i].testResult < children[i+1].testResult:
                current_cookie = current_cookie + 1
            else:
                current_cookie = 1

            i = i+1

        current_cookie = 1

        i = len(children)-1
        while i >= 0:
            children[i].cookiez = max(current_cookie, children[i].cookiez)

            if i == 0:
                break

            if children[i].testResult < children[i-1].testResult:
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
            print("pos: " + str(pos) + " cookiez: " + str(child.cookiez) + " test result: " + str(child.testResult) + "\n")


    def add_or_remove_cookie(self, cookies):
        if (random.randint(0, 1) == 1):
            return cookies - 1
        else:
            return cookies + 1

    def mutate(self, children):
        for child in children:
             rolled_value = random.randint(0, 100)
             if (rolled_value <= self.base_mutation_chance):
                 child.cookiez = self.add_or_remove_cookie(child.cookiez)

        return children

    def mutate_with_decreasing_chance(self, children):
        chance = self.base_mutation_chance
        for child in children:
            rolled_value = random.randint(0, 100)
            if (rolled_value <= chance):
                child.cookiez = self.add_or_remove_cookie(child.cookiez)
                chance = chance/2

    #mutation is a function
    def mutate_population(self, population, mutation):
        mutated = list(map(lambda children: mutation(children), population))
        return mutated
                
    def get_fitness(self, children):
        cookie_sum = sum(abs(child.cookiez) for child in children)
        bad_pos_count = 0
        for i in range(1, len(children)):
            child1 = children[i-1]
            child2 = children[i]
            if child1.testResult < child2.testResult:
                if child1.cookiez >= child2.cookiez:
                    bad_pos_count += 1
            elif child1.testResult > child2.testResult:
                if child1.cookiez <= child2.cookiez:
                    bad_pos_count += 1
            elif child1.cookiez < 1:
                bad_pos_count += 1
        if children[-1].cookiez < 1:
            bad_pos_count += 1
        
        return cookie_sum + bad_pos_count * self.punishment_factor
    
    def all_with_all_breeding(self, population, crossover):
        for pair in itertools.combinations(population, 2):
            yield crossover(pair[0], pair[1])
    
    def random_breeding(self, population, how_many_children, crossover):
        for i in range(how_many_children):
            random_pair = random.choices(population, k = 2)
            yield crossover(random_pair[0], random_pair[1])

    def select_k_best(self, population, k):
        return selection.k_best(population, k, self.get_fitness)

    def select_weighted(self, population, k):
        return selection.weighted(population, k, self.get_fitness)

