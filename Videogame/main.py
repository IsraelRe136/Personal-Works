import pygame
import sys
import GameUtilities
import numpy as np 
import time




"""
Homework 6 - pygame

Author: Miguel Angel Verdi Resendiz, verdi.resendiz.miguel@gmail.com
Description:  This algorithm has to be run with the GameUtilities library,
is a videogame that generates obstacles and the playes has to avoid them
If you crash 5 times with the asteoird, the game is over  
"""





pygame.init()


#Initial parameters of the display screen
screen_w, screen_h = 640,480
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()
TICK = 100 
RESIZED = 100


#Creates the objet rocket, and get the rectangle of boundaries 
rocketIMG = pygame.image.load('rocket.png')
rocketIMG = pygame.transform.scale(rocketIMG,(RESIZED, RESIZED))

#The rectange starts in the botton
rocket_rect = rocketIMG.get_rect()
rocket_rect.top = screen_h - rocket_rect.height 



#Initialization of the background image 
background = pygame.image.load('background.png')
background = pygame.transform.scale(background,(screen_w, screen_h))
Background = GameUtilities.Background(background, screen,screen_w,screen_h)

#Change in the rocket x position
x_change = 0
rocket_Move = GameUtilities.move(screen_w,screen_h,rocket_rect.width, rocket_rect.height)



#We charge the asteorid image, and get the rectangle of it.
Asteroid = pygame.image.load('asteroid.png')
Asteroid = pygame.transform.scale(Asteroid,(40,40))
Asteroid_rect = Asteroid.get_rect()


#Creating the asteorid move object
Asteoroid_move = GameUtilities.move(screen_w, screen_h, Asteroid_rect.width, Asteroid_rect.height)

 

#Here we create 5 asteroids with a rectanlge each
#This method gives a list with a number of rectangles that represents the position of each asteroid
number_of_asteroids = 8
Asteroids = GameUtilities.asteroids(Asteroid_rect, number_of_asteroids,screen_w, screen_h)
                   
              
                
#Initial positions of asteroids (randomized)              
Asteroids_rectangels = Asteroids.create_boxes()                                 

T0 = time.time()

#Parameters
WHITE = (255,255,255)
BLUE = (0,0,255)

crashed = False
y_speed = 4 #Falling speed
SCORE = 5
COLLISION = False


while not crashed:
   
    
   #Reads if there is an action in the keyboard.
    for event in pygame.event.get():    
      
        if event.type == pygame.QUIT:
            crashed = True
            pygame.quit()
            sys.exit()            
            
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                x_change = -4
            elif event.key == pygame.K_RIGHT:
                x_change = 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            
            
  
      
   

    
    
    
    #Update the rocket coordinates when pressing any key
    x_coordinate = rocket_Move.x_move(x_change,rocket_rect.centerx)  
    rocket_rect = rocket_rect.move(x_coordinate,0)
    
    
    
    
    
    #Creating the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, WHITE, rocket_rect)
    
    
    
    
    #Scroling image and rocket 
    Background.scroll()
    
    
    
    
    #Blit of the rocket
    screen.blit(rocketIMG, rocket_rect)

    
          
    
    


    #Ateroids printing, it iterates in a list of Asteroids_rectangels that contains
    #All the positional rectangles.
    for position in Asteroids_rectangels: 
        screen.blit(Asteroid,position)
        
    
   

    
    
    #This loop looks thorught all the asteroid boxes,
    #And cheks if the asteroid is colliding with the rocket.    
    for asteroid in Asteroids_rectangels:

        if rocket_rect.top <= asteroid.bottom :
            
            
            if asteroid.left <= rocket_rect.right and rocket_rect.right <= asteroid.right:
                COLLISION = True
            
            if asteroid.left <= rocket_rect.left and rocket_rect.left <= asteroid.right:
                COLLISION = True
            
            if asteroid.right <= rocket_rect.right and  asteroid.left >= rocket_rect.left:
                COLLISION = True
            
          
            
    
        
    
    
    
    #Asteroids update:  
    #Uptates the asteroids positions, it considers when the asteroids have reached the botton
    #And If they have, creates new asteroids with random positons
    if Asteroids_rectangels[0].bottom < screen_h  : 
        y_cordinate = Asteoroid_move.y_move(y_speed, Asteroid_rect.centery)
        
        for i,asteorid_rectangle in enumerate(Asteroids_rectangels): 
          
            asteorid_rectangle = asteorid_rectangle.move(0,y_cordinate)
            Asteroids_rectangels[i] = asteorid_rectangle
    
    else:
        
        Asteroids_rectangels = Asteroids.create_boxes()    
        
        
        #We update the score only when the asteroids have went to the bottom
        if COLLISION == True: 
            SCORE -= 1
            COLLISION = False
            
    
    
    
    
    
    
    #This fills the screen with a legend game over, then waits 5 seconds and closes the screen
    if SCORE == 0: 
        screen.fill(BLUE)
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'GAME OVER', True, (255, 255, 255))
        screen.blit(score_text, (screen_w/2, screen_h/2))
        
        
        T1 = time.time()
        
        if T1 - T0 > 5:
            crashed = True
            pygame.quit()
            sys.exit()
        
            
        
        
    #Plots the score in the screen
    if SCORE > 0:
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {SCORE}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
         
    
        
    
        
        
        
    
    
    pygame.display.update()
    clock.tick(TICK)
    
    
  
   
    
    
    
    
    
    

pygame.quit()