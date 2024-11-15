import numpy as np

# 杂交
def crossover(parents, pc):
    offspring = []
    parents_len = len(parents)

    for i in range(0, parents_len, 2):
        p1 = parents[i]
        if i + 1 < parents_len:
            p2 = parents[i + 1]
        else:
            p2 = parents[0]

        if np.random.rand() < pc:
            point = np.random.randint(1, len(p1))
            c1 = np.concatenate((p1[:point], p2[point:]))
            c2 = np.concatenate((p2[:point], p1[point:]))
        else:
            c1 = p1.copy()
            c2 = p2.copy()

        offspring.append(c1)
        offspring.append(c2)

    return np.array(offspring)