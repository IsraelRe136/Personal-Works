import matplotlib
from random import random 
from pylab import *
import networkx as nx



def initial_conditions(n,e): 
    
    global network, status, positions
    #Generates a random network  nodes,  edges
    network = nx.gnm_random_graph(n, e)
    status = []
    
    for i in network: 
        network.nodes[i]['status'] = random()
        status.append(network.nodes[i]['status'])

    positions = nx.spring_layout(network)
    
    #nx.draw(network,positions,cmap = cm.gray,vmin =0,vmax =1,node_color = status)
     
    #show()
    return network,positions
    
    
def evolution(n,alpha,dt,t):
    
    global network, status, positions

    time = 0 
    status = []
    s= 0
    sume = 0 
    iterations = int(t/dt)
    print(iterations)
    for k in range(iterations): 
        time += dt
        for i in network:
            for j in  network.neighbors(i):
                s += network.nodes[j]['status']
                
            network.nodes[i]['status'] += alpha*dt*(s-network.nodes[i]['status']*network.degree(i))
            
            status.append(network.nodes[i]['status'])
            
            sume += network.nodes[i]['status']
            
            s = 0
            
        
        if k%200 == 0:
            nx.draw(network,positions,cmap = cm.gray,vmin =0,vmax =1,node_color = status)
            text = 'Dynamical network at time: ' + str(round(time,4))  + 's.'
            title(text)
            show()
            text2 = 'Tiempo: ' + str(round(time,4))  + 's.' + 'Suma: ' + str(sume)
            print("---------")
            print(text2) 
        
            print("---------")
            
        sume = 0
        status = []
        

n = 30
e = 100
dt = 0.01
alpha = 0.009
t = 11



net, pos = initial_conditions(n,e)
evolution(n,alpha,dt,t)
     
       
    
    

