import numpy as np

# 初始化种群
def init_population(population_size, gene_size, gene_count):
    return np.random.randint(0, 2, (population_size, gene_size * gene_count))