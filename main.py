from function.fitness_function import fitness_function
from population import init_population

bounds = [0, 6]
population_size = 1000
gene_size = 23
gene_count = 2

def main():
    population = init_population(population_size, gene_size, gene_count)
    print("初始种群：")
    print(population)

    fitness = fitness_function(population, bounds, gene_size)
    print("适应值：")
    print(fitness)





if __name__ == "__main__":
    main()