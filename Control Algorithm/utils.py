"""
Utility functions for pygame simulator ('simulator.py')
"""
import numpy as np
import matplotlib.pyplot as plt

def solver(x, v_x, c, m, f, delta_t, x_max, x_img_size, padding = 0):

    x_new = x + v_x*delta_t # new x position calculation
    v_new = v_x - (c / m) * v_x * delta_t + (f / m) * delta_t # new x velocity calculation

    # check boundaries. If the system is at the boundary then: x(k+1) = x(k) and new velocity is 0
    if x_new + x_img_size//2 +padding > x_max:
        return x, 0
    elif x_new + x_img_size//2 < 0:
        return x, 0
    else:
        return x_new, v_new



def controller(e,K_p,K_d,K_i,dt,I):
  
    #The array error uses the past errors that are stored in an array
    #e[0] -> e(t-2), e[1] -> e(t-1), e[2] -> e[t]
    
    
    #The proportional term of controler
    P = K_p*e[2] 
    
    #The derivative term with Taylor 
    D = (K_d/(2*dt))*(3*e[2] - 4*e[1] + e[0])
    
    #Integral term with the rectanble formula
    I += K_i*dt*e[2] 
   
    
    #Sum of PID and get the force
    u = P + D + I
    
    
    return u,I

    

    


def update_line(plot, new_data, time_step):
    
    plot.set_xdata(np.append(plot.get_xdata(), new_data[0]))
    plot.set_ydata(np.append(plot.get_ydata(), new_data[1]))
   
   
    plt.pause(time_step)    # update graph every 0.5 second
    
    
    
    
    