import numpy 
import math
import graph

def cross(mother,father):
    my_len_m=(len(mother.nodes)-1)//2
    my_len_f=(len(father.nodes)-1)//2
    child=[1,2]
    while(math.log(len(child)+1,2) != (int)(math.log(len(child)+1,2))):
        start_m = numpy.random.randint(0,my_len_m)
        start_f = numpy.random.randint(0,my_len_f)
        end_m = numpy.random.randint(start_m,my_len_m)
        end_f = numpy.random.randint(start_f,my_len_f)
        child = mother.nodes[:start_m] + father.nodes[start_f : end_f] + mother.nodes[end_m : my_len_m]   
    for i in range(len(child)+1):
        node=graph.Node('x')
        child.append(node) 
    return child        
