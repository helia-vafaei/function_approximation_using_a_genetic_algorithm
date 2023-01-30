class Node:
    def __init__(self, data):
        self.children = []
        self.data = data 

class Graph:
    def __init__(self):
        self.nodes=[]
        self.fitness=0
    def add_root(self,node):
        self.nodes.append(node) 
    def add_child(self,node,parent):
        self.nodes.append(node)
        parent.children.append(node)




