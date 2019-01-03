from algorithm import Algorithm
from child import Child
import random

max_grade = 10
max_cookiez = 11
algo = Algorithm()

def generate(count):
    results = []
    cookiez = []

    for x in range(count):
        results.append(random.randint(0, max_grade))
        cookiez.append(random.randint(0, max_cookiez))

    zipped = zip(results, cookiez)
    zipped = list(map(lambda result, cookie: Child(int(result), int(cookie)), zipped))

    return zipped

# array of ints
def generate_tests_results_only(count):
    results = []

    for x in range(count):
        results.append(random.randint(0, max_grade))

    return results


def generate_cookiez_only(count):
    cookiez = []

    for x in range(count):
        cookiez.append(random.randint(0, max_cookiez))

    return cookiez

def generate_cookiez_for_test_results(test_results):
    cookiez = generate_cookiez_only(len(test_results))

    zipped = zip(test_results, cookiez)
    zipped = list(map(lambda result, cookie: Child(int(result), int(cookie)), zipped))

    return zipped

# cos co wywola robienei dzieci
# kryterium stop
# mierzenie czasu benchmark
# rozne parametry