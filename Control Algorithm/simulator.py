

"""
Homework 7 - Control

Author: Miguel Angel Verdi Resendiz, verdi.resendiz.miguel@gmail.com
Description:  This algorithm controls a model of a damped system, the sistem is described in utils, and the 
control algoritm is a PID, the position is ploted an the force (to switch press the up-key)
"""



import pygame
import matplotlib.pyplot as plt
import random
import numpy as np
from utils import solver, controller, update_line




#Parameters
x_desired = 200

#PID parameters
K_p =  1.
K_d = 0.5
K_i = 0.1




# IMPORTANT GAME CONSTANTS
WIDTH = 800 # display widht
HEIGHT = 600 # display height
TICK = 40 # framerate: frames per second
GAME_CAPTION = "Control simulation"
RESIZED = 200 # pixels of rocket IMG
ROCKET_IMG_PATH = "rocket.png"


# BASIC COLOURS
# It's usefull to define them as constants, we can use
# them reapeatedly
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)



if __name__ == "__main__":
    # initialize updating plot
    plot, = plt.plot([], [])  # empty plot
    plot2, = plt.plot([], [], label = 'Desired position')  

    
    t_sim = 30
    # set axis limits
    plt.xlim(0, t_sim) # 30 seconds of simulation will be visualized
    plt.ylim(0, WIDTH) # the range of x position will be visualized
    # title, labels
    plt.title("x position of the rocket in time")
    plt.xlabel("time [s]")
    plt.ylabel("x position [px]")

    pygame.init() # inits all important pygame modules for us
    pygame.font.init() # fonts
    myfont = pygame.font.SysFont('Arial',50)

    game_display = pygame.display.set_mode((WIDTH, HEIGHT)) # create game display
    pygame.display.set_caption(GAME_CAPTION) # set caption
    clock = pygame.time.Clock() # initilize clock

    # Load and prepare our image of rocket
    rocket_img = pygame.image.load(ROCKET_IMG_PATH)
    rocket_img = pygame.transform.scale(rocket_img,(RESIZED, RESIZED))
    rocket_img = pygame.transform.rotate(rocket_img, 90) # rotate img 90 degrees

    # Initial position of a rocket - bottom center
    x = int((WIDTH - RESIZED)/2) # initial coordinate x
    y = int(HEIGHT - RESIZED - 200) # initial coordinate y

    # initial conditions
    force = 0 # initial force is zero
    max_wind_force = 30  # maximum wind disturbance force [N]
    velocity = 0 # initial velocity
    delta_t = 1/TICK #time step of simulation = 1/framerate

    # parameters of controlled system
    weight = 1 # weight [kg]
    damping = 0.5 #damping parameter [kg/s]
        
    
    
      
    #Initial parameters of error. 
    #e[0] -> e(t-2), e[1] -> e(t-1), e[2] -> e[t] 
    I = 0
    e = [x_desired - x,x_desired - x,x_desired - x]
   
    
   
    #Plot the desired x position.
    plot2.set_data([[0,t_sim],[x_desired,x_desired]])
  

    #A varariable of ploting force or position.
    plot_force = False
    
    # main while loop
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                crashed = True # if we pressed cross, game will end
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    force = -50
                elif event.key == pygame.K_RIGHT:
                    force = 50
            
            if event.type == pygame.KEYDOWN:
                #plt.clf()
                plt.cla()
                
                #Plot 1, for x position, plot 2 for desired position, plot 3 for force
                plot, = plt.plot([], [])
                plot2, = plt.plot([], [])  
                plot3, = plt.plot([], []) 
                
                
                if event.key == pygame.K_UP:
                   
                    
                    #If Kup pressed the position is printed
                    plot2.set_data([[0,t_sim],[x_desired,x_desired]])
            
                    plt.xlim(0, t_sim) 
                    plt.ylim(0, WIDTH) # the range of x position will be visualized
                    plt.title("x position of the rocket in time")
                    plt.xlabel("time [s]")
                    plt.ylabel("x position [px]")
                    
                    plot_force = False 
                    
                    
                    
                elif event.key == pygame.K_DOWN:
                    
                    #iF k_DOWN pressed the force is printed
                    
                    plt.xlim(0, t_sim) # 30 seconds of simulation will be visualized
                    plt.ylim(-100, 100) # the range of x position will be visualized
                    plt.title("Force on the rocket in time")
                    plt.xlabel("time [s]")
                    plt.ylabel("Force [N]")
                    
                    
                    plot_force = True
            
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    force = 0

        # random force disturbance
        force_disturbance = random.uniform(0, max_wind_force)



        
        #Here we get the force of the controler, we need the past I to calculate the integral
        force,I = controller(e,K_p,K_d,K_i,delta_t,I)
        
        
        #Update the error vector 
        #e[0] -> e(t-2), e[1] -> e(t-1), e[2] -> e[t]
        e[0] = e[1]
        e[1] = e[2]
        e[2] = x_desired - x #Courrently error.
        
        
        

        # sum of controlling force and force disturbance
        total_force = force + force_disturbance

        # call the solver - calculate x position and velocity
        x, velocity = solver(x, velocity, damping, weight, total_force, delta_t, WIDTH, RESIZED)
                
        # GRAPHIC
        #   fill screen with white colour
        game_display.fill(WHITE)



          
        #Draws the desired position of the rectangle
        pygame.draw.rect(game_display, BLACK, pygame.Rect(x_desired, HEIGHT/2 - 20  ,5 , 40))
        
        
        
        
        #Draws the an arrow representing the force 
        pygame.draw.line(game_display, RED, (x,y), (x + force_disturbance,y), width=5)
        
        Arrow_coordinates = ((x + force_disturbance + 1, y),
                             (x + force_disturbance - 5 + 1, y + 10) ,
                             (x + force_disturbance - 5 + 1, y - 10))
        
        pygame.draw.polygon(game_display, RED,Arrow_coordinates)
        
      
        
        # show image of rocket in position x,y
        game_display.blit(rocket_img,(x,y))
        pygame.display.update()
        simulation_time = pygame.time.get_ticks()/1000
        
        
        
     
        
        
        
         #Here we decide with of the plots to plot.   
        if plot_force == False: 
      
            update_line(plot, [simulation_time, x], delta_t)
            plt.draw()
         
            
         
        
        if plot_force == True:
           
            update_line(plot3, [simulation_time, force], delta_t)
            plt.draw()


        
        
        clock.tick(TICK)

    pygame.quit()  