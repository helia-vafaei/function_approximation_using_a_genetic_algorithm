FUNCTIONS = ['+', '-', '*', '/']

def eval(gen,x,poz=0):
    if(gen.nodes[poz].data == 'x'):
        return x , poz
    if(gen.nodes[poz].data in FUNCTIONS):
        poz_op = poz
        left , poz = eval(gen,x,poz+1)    
        right , poz = eval(gen,x,poz+1) 
        if(gen.nodes[poz_op].data == '+'):
            return left + right, poz
        elif(gen.nodes[poz_op].data == '-'):
            return left - right, poz
        elif(gen.nodes[poz_op].data == '*'):
            return left * right, poz  
        elif(gen.nodes[poz_op].data == '/'):
            if right!=0:
                return left / right, poz    
            return left/0.01,poz               
