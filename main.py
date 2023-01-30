import random
import time
import numpy
import matplotlib.pyplot as plt
import make_random_graphs
import evaluate
import fitness
import selection
import cross_over
import return_best
import graph

start = time.time()
FUNCTIONS = ['+', '-', '*', '/']

def func(x):
    return x-x*x

X = [x for x in numpy.arange(0, 10, 0.01)]   
Y = [func(x) for x in X] 

# depth=random.randint(3,5)  
# main lines for calculating depth is line 20 but it takes a long time to run the program so we assume depth is 1.
depth=1     
gens = make_random_graphs.random_graphs(depth)   
population=[]
evals=[]
amount=0

for g in gens:
    evals=[]
    for x in X:
        evals.append(evaluate.eval(g,x,0)[0])
    g.fitness = fitness.fit(evals , Y)
    amount=amount+1

size = len(gens)//2    
for i in range(200):
    mother = selection.select(gens,size)              
    father = selection.select(gens,size)  
    child = cross_over.cross(mother,father)   
    g_child=graph.Graph()
    g_child.nodes=child
    evals=[]     
    for x in X:
        evals.append(evaluate.eval(g_child,x,0)[0])
    g_child.fitness = fitness.fit(evals , Y)    
    amount=amount+1          
    population.append(g_child)
res=return_best.best(population)
for i in res.nodes:
    print(i.data)
print(f"fitness is {res.fitness}")
print(f"amount of calculating fitness is {amount}")
print(f"amount of descendant is {2}")


plt.plot(X, evals, color='r', dashes=[6, 3])
plt.plot(X, Y, color='b', dashes=[6, 2])
plt.show()

end = time.time()
print(f"Runtime of the program is {end - start}")