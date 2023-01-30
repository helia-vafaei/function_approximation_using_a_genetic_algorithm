import main
import random

def mutate(g,depth):
    poz=random.randint(0,(2**depth)-1)
    if len(g.nodes[poz].children) == 2:
        g.nodes[poz]=random.choice(main.FUNCTIONS)
    return g    