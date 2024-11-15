import numpy as np

from function.fitness import fitness_function
from operators.crossover import crossover
from operators.mutation import mutation
from selection.roulette_wheel import roulette_wheel_selection


def ga(population, bounds, gene_size, pc, pm):
    fitness = fitness_function(population, bounds, gene_size)

    parents = roulette_wheel_selection(population, fitness)
    offspring = crossover(parents, pc)

    mutated_offspring = mutation(offspring, pm)
    combined_population = np.vstack((population, mutated_offspring))

    fitness = fitness_function(combined_population, bounds, gene_size)
    best_index = np.argsort(-fitness)[:len(population)]
    new_population = combined_population[best_index]

    return new_population

