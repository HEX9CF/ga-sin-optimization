import numpy as np

from function.objective_function import objective_function

# 解码
def decode(binary, bounds, gene_size):
    decimal = int("".join(map(str, binary)), 2)
    return bounds[0] + (bounds[1] - bounds[0]) * decimal / (2**gene_size - 1)

# 适应值函数
def fitness_function(population, bounds, gene_size):
    fitness = []
    for i in population :
        x1_binary = i[:gene_size]
        x2_binary = i[gene_size:]

        x1 = decode(x1_binary, bounds, gene_size)
        x2 = decode(x2_binary, bounds, gene_size)

        fitness_value = objective_function([x1, x2])
        fitness.append(fitness_value)
    return np.array(fitness)

