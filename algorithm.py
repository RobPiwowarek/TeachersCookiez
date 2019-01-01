import random

class Algorithm:
    base_mutation_chance = 20

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

    def print_optimal(self, children):
        result = self.calculate_optimal(children)


        for pos, child in enumerate(result):
            print("pos: " + str(pos) + " cookiez: " + str(child.cookiez) + " test result: " + str(child.testResult) + "\n")


    def add_or_remove_cookie(self, cookies):
        if (random.randint(0, 2) == 1):
            return cookies - 1
        else:
            return cookies + 1

    def mutate(self, children):
        for child in children:
             rolled_value = random.randint(0, 101)
             if (rolled_value <= self.base_mutation_chance):
                 child.cookiez = self.add_or_remove_cookie(child.cookiez)

        return children

    def mutate_with_decreasing_chance(self, children):
        chance = self.base_mutation_chance
        for child in children:
            rolled_value = random.randint(0, 101)
            if (rolled_value <= chance):
                child.cookiez = self.add_or_remove_cookie(child.cookiez)
                chance = chance/2