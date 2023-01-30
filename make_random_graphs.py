import random
import graph

FUNCTIONS = ['+', '-', '*', '/']
gens=[]

def make(g,p,x,num_of_nodes):
    if(x==num_of_nodes):
        x1=graph.Node('x')
        x2=graph.Node('x')
        g.add_child(x1,p)
        g.add_child(x2,p)
        return
    my_random1=random.choice(FUNCTIONS)
    n1=graph.Node(my_random1)
    my_random2=random.choice(FUNCTIONS)
    n2=graph.Node(my_random2)
    g.add_child(n1,p)
    g.add_child(n2,p)
    make(g,n1,x+1,num_of_nodes)
    make(g,n2,x+1,num_of_nodes)

def random_graphs(depth):
    for i in range(200):
        my_random=random.choice(FUNCTIONS)
        r=graph.Node(my_random)
        g = graph.Graph()
        g.add_root(r)
        x=0
        num_of_nodes=(2**depth)-1
        make(g,r,x,num_of_nodes)   
        gens.append(g)
    return gens
