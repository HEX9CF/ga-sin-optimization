import numpy as np

# 变异
def mutation(offspring, pm):
    for i in range(len(offspring)):
        for j in range(len(offspring[i])):
            if np.random.rand() < pm:
                # 翻转二进制位
                offspring[i][j] = 1 - offspring[i][j]
    return np.array(offspring)