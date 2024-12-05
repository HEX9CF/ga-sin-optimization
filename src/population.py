import numpy as np

# 初始化种群
def init_population(pop_size, gene_size, gene_count):
    return np.random.randint(0, 2, (pop_size, gene_size * gene_count))