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
    file = open(file_name)
    for child in result:
        file.write(str(child.testResult) + " ")

    file.write(": ")

    for child in optimal_result:
        file.write(str(child.testResult) + " ")
    file.write("\n")
    file.close()
