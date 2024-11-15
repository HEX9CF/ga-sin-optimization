import numpy as np

from function.fitness import fitness_function, decode
from ga import ga
from population import init_population
from matplotlib import pyplot as plt

bounds = [0, 6]     # 取值范围
pop_size = 64     # 种群数量
gene_size = 23      # 基因长度
gene_count = 2      # 基因数量
pc = 0.75           # 杂交概率
pm = 0.4           # 变异概率
max_epoch = 10000        # 最大迭代次数
max_best_unchanged_epoch = 100 # 最好个体未发生变化代数

def main():
    max_fitness = []
    avg_fitness = []

    # 初始种群
    population = init_population(pop_size, gene_size, gene_count)

    best_unchanged_epoch = 0
    max_fitness.append(np.max(fitness_function(population, bounds, gene_size)))
    avg_fitness.append(np.mean(fitness_function(population, bounds, gene_size)))

    for i in range (max_epoch):
        epoch = i + 1
        print("第", epoch, "代：")
        population = ga(population, bounds, gene_size, pc, pm)
        print("种群数量：", len(population))

        max_fitness.append(np.max(fitness_function(population, bounds, gene_size)))
        avg_fitness.append(np.mean(fitness_function(population, bounds, gene_size)))
        print("平均适应值：", avg_fitness[epoch])
        print("最大适应值：", max_fitness[epoch])

        plt.subplot(1, 2, 1)
        plt.plot(max_fitness, label='max')
        plt.plot(avg_fitness, label='avg')

        if max_fitness[epoch] == max_fitness[epoch - 1]:
            best_unchanged_epoch+=1
        else:
            best_unchanged_epoch = 0

        # 最好个体在n代内是否发生变化
        print("最好个体未发生变化代数：", best_unchanged_epoch)
        if best_unchanged_epoch >= max_best_unchanged_epoch:
            break

    # 输出全局最优解
    print("全局最优解：")
    fitness = fitness_function(population, bounds, gene_size)
    for epoch in range(len(population)):
        x1_binary = population[epoch][:gene_size]
        x2_binary = population[epoch][gene_size:]

        x1 = decode(x1_binary, bounds, gene_size)
        x2 = decode(x2_binary, bounds, gene_size)

        plt.subplot(1, 2, 2)
        print("x1:", x1, "x2:", x2, "f(x):", fitness[epoch])
        plt.scatter(x1, x2)

    # 绘图
    plt.subplot(1, 2, 1)
    plt.xlabel('epoch')
    plt.ylabel('fitness')
    plt.title("fitness")

    plt.subplot(1, 2, 2)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title("result")
    plt.show()

if __name__ == "__main__":
    main()