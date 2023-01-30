def best(population):
    best = population[0]
    for i in range(len(population)):
        if population[i].fitness < best.fitness:
            best = population.list[i]
    return best