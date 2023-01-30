import random

def select(gens,size):  
    sample = random.sample(gens, size)
    best = sample[0]
    for i in range(size):
        if sample[i].fitness < best.fitness:
            best = sample[i]
    return best
