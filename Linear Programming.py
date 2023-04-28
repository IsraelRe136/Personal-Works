import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd



"""
Title: cvxpy, optimization, linear programming

Author: Miguel Angel Verdi Resendiz, verdi.resendiz.miguel@gmail.com
Description:  This algorithm uses the library cvxpy to optimaze the profit 
of a factory that is producing 3 diferent products
"""


#Specifications of the product's prices
price_a = np.full(12, 325.)


price_b = np.array([300, 300, 290, 275, 275, 280,
                    260, 250, 230, 200, 210, 190.])


price_c = np.array([100, 110, 98, 115, 200, 220,
                    210, 500, 500, 490, 487, 550.])




#A dictionary to create the data frame, empty at the beginning
data = {'Month': ['Jan','Feb','Mar','Apr',
          'May','Jun','Jul','Aug','Sep',
		'Oct','Nov','Dec'],
          'Pieces of A': np.zeros(12),
          'Pieces of B': np.zeros(12),
          'Pieces of C': np.zeros(12),
          'Profit': np.zeros(12)
        }

df = pd.DataFrame(data)



#4 arrays to save the calculations of the algorithm
pieces_of_A = []
pieces_of_B = []
pieces_of_C = []
profit = []


#We iterate in each moth so each iteration we get 4 quantities,
#products per month, and profit per month
for n_month,month in enumerate(df['Month']):
    
    
    prices = [price_a[n_month], price_b[n_month],price_c[n_month]] #Prices in determinated month (a,b,c)
    
    pieces = cp.Variable(3) #Number of pieces in a month (a,b,c) 
    

    
    constraints = [
        
        cp.sum(pieces) <= 10000,
        pieces >= 2000,
        pieces[2] <= 5000 if n_month > 5 else True,
        pieces[1] <= 4500,
        pieces[0] <= 4000 if n_month < 5 else True,
               
    ]#Conditions that the problem specified. 
    
    
    
    objective = cp.Maximize(prices*pieces)
    problem = cp.Problem(objective, constraints)    
    problem.solve(verbose=True)
    

    #Saves the values of number of products
    pieces_of_A.append(pieces.value[0])
    pieces_of_B.append(pieces.value[1])
    pieces_of_C.append(pieces.value[2])
    
    
    profit.append(sum(prices*pieces.value))
    


#We fill the data frame, having all the arrays
df['Pieces of A'] = pieces_of_A
df['Pieces of B'] = pieces_of_B
df['Pieces of C'] = pieces_of_C
df['Profit'] = profit 

#Pints the data frame
print(df)
print(f"Total profit of the next year: {round(df.sum(axis = 0)['Profit'])}")




#We plot the information of the number of products that should be made.
fig, ax = plt.subplots(3 , sharey = True)

ax[0].bar(df['Month'], df['Pieces of A'], color = 'red')
ax[0].set_title('Product A') 
ax[1].bar(df['Month'], df['Pieces of B'], color = 'blue')
ax[1].set_title('Product B') 
ax[2].bar(df['Month'], df['Pieces of C'], color = 'green')
ax[2].set_title('Product C') 

for i in range(3):
    ax[i].set_ylabel('N of products')
    ax[i].grid(True)
    
fig.suptitle(f"Total profit of the next year: {round(df.sum(axis = 0)['Profit'])}") # or plt.suptitle('Main title')

fig.set_figheight(7) 
fig.set_figwidth(10) 
fig.subplots_adjust(hspace = 0.8) 
plt.show()

    