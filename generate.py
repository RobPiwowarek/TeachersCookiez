from algorithm import Algorithm
from child import Child
import random

max_grade = 10
algo = Algorithm()


# generate in the format number number number ....
def generate(count):
    population = []
    for x in range(count):
        population.append(random.randint(0, max_grade + 1))

    population = list(map(lambda test_result: Child(test_result), population))

    return population


# generate in the format number, number, number : number number number ...
# corresponding to generated : optimal
def generate_to_file_with_optimal(count, file_name):
    population = generate(count)
    optimal = algo.calculate_optimal(population)

    save_with_optimal(file_name, population, optimal)


def save(file_name, result):
    file = open(file_name, "w")
    for child in result:
        file.write(str(child.testResult) + " ")
    file.write("\n")
    file.close()


def save_with_optimal(file_name, result, optimal_result):
    file = open(file_name, "w")
    for child in result:
        file.write(str(child.testResult) + " ")

    file.write(": ")

    for child in optimal_result:
        file.write(str(child.testResult) + " ")
    file.write("\n")
    file.close()


def load(file_name):
    with open(file_name, "r") as file:
        for line in file:
            values = line.split(' ')
            file.close()
            return list(map(lambda value: Child(int(value)), values))


def load_with_optimal(file_name):
    with open(file_name, "r") as file:
        for line in file:
            results = line.split(':')
            generated = results[0].split(' ')
            optimal = results[1].split(' ')

            generated = list(map(lambda value: Child(int(value)), generated))
            optimal = list(map(lambda value: Child(int(value)), optimal))
            file.close()
            return (generated, optimal)

def load_multiple(file_name):
    generated_populations = []

    with open(file_name, "r") as file:
        for line in file:
            values = line.split(' ')
            generated_populations.append(list(map(lambda value: Child(int(value)), values)))

    file.close()
    return generated_populations

def load_multiple_with_optimal(file_name):
    generated_populations = []

    with open(file_name, "r") as file:
        for line in file:
            results = line.split(':')
            generated = results[0].split(' ')
            optimal = results[1].split(' ')

            generated = list(map(lambda value: Child(int(value)), generated))
            optimal = list(map(lambda value: Child(int(value)), optimal))

            generated_populations.append((generated, optimal))

    file.close()
    return generated_populations