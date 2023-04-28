import matplotlib.pyplot as plt
import threading
import numpy as np 
import time 
import pandas as pd


"""
Title: multithreading


Author: Miguel Angel Verdi Resendiz, verdi.resendiz.miguel@gmail.com
Description:  This program computes a function with 3 threads, for calculate the y(x) 
points 'calculate', for ploting 'plot', and for write in a cvs file 'write'  
"""





global initial_time
global x
global y 
global X_vector
global Y_vector


#Variables x,y for calculation in each step, and the vectors for creating the data frame
#and the plot
x,y = 0,0
X_vector,Y_vector = [],[]
lock = threading.Lock()



#The time of simulation stops the process
initial_time = time.time()
time_of_simulation = 30



#Generic function for ploting a function of x,y, pauses for 2 seconds
def function_plot(X_,Y_):           
    plt.plot(X_,Y_,'b.')
    plt.draw()
    plt.ylim(-10, 10)       
    plt.xlim(0, time_of_simulation)
    plt.xlabel('X variable')
    plt.ylabel('Y variable')
    Actual_time = time.time() - initial_time 
    plt.title(f'Plot of the function at {round(Actual_time,2)}s')
    plt.grid()
    plt.pause(2)



#Function of ploting to make the thread
def Function_ploting_thread():
    with lock:        
        while time.time() - initial_time < time_of_simulation : 
            function_plot(X_vector,Y_vector)
           
            
           
            
#function to update the calculation and vectors of results         
def Function_calculation():

    #We use global to modify/use in the whole program
    global x,y, X_vector, Y_vector
    
    
    while time.time() - initial_time < time_of_simulation : 
        
        #The main calculation of the function, it just calculates 
        # A sin function each step. 
        
        x += 0.2
        y = 5*np.sin(x)
        
        X_vector.append(x)
        Y_vector.append(y)
            
        time.sleep(1)
        

#This function writes the csv, first it creates a data frame of the vectors.
def Function_write():
    
    global x,y
    
    while time.time() - initial_time < time_of_simulation : 
        
        
        DF = pd.DataFrame(data = [X_vector,Y_vector], index = ["X_data", "Y_data"])
        DF.to_csv("Data_of_function.csv")
        
        time.sleep(3)





if __name__ == "__main__":

    Calculate = threading.Thread(target= Function_calculation)
    Write = threading.Thread(target= Function_write)
    Plot = threading.Thread(target= Function_ploting_thread)
    
    
    Calculate.start()
    Write.start()
    Plot.start()
    
    Calculate.join()
    Write.join()
    Plot.join()
    
    print(f'Elapsed time: {time.time() - initial_time}' )

    
    
