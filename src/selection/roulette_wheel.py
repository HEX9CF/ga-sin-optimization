import numpy as np

# 轮盘赌选择
def roulette_wheel_selection(population, fitness):
    # 适应值总和
    fitness_sum = np.sum(fitness)

    # 相对适应值
    rel = fitness / fitness_sum

    # 个体繁殖量
    n = np.round(rel * len(population))

    parents = []
    for i in range(len(n)):
        parents.extend([population[i]] * int(n[i]))

    return np.array(parents)
