import pygame
import random 
import numpy as np 



#I made this library in order to make easy the programming
class asteroids: 
    
    def __init__(self,Asteoroid_box, n, w,h ):       
        self.Asteoroid_box = Asteoroid_box
        self.n = n 
        self.width = w

    #This function creates an array of positions for the boxes with random x position but y position
    # defined as y = 100, this can be change to a variable in furter aplications
    def create_boxes(self):
            
        Boxes = []
        for i in range(self.n): 
            box  = self.Asteoroid_box.copy() 
            box.center = (random.randint(0 + self.Asteoroid_box.width/2, self.width),100)
            Boxes.append(box)
        return Boxes





#this Class just takes the actual position of a box, some parameters of the screen
#And of the object, and returns the changes for moving the object, but considereing 
#boundaries.
class move:
    
    def __init__(self,x_boundary,y_boundary,width,height):
        self.x_boundary = x_boundary 
        self.y_boundary = y_boundary 
        self.width = width
        self.height = height
        
    
        
    def x_move(self,x_change, x_center):

        if x_change > 0: 
            
            if x_center + self.width/2  <= self.x_boundary: 
                return x_change
            else: 
                return 0
            
        elif x_change < 0: 
            if x_center - self.width/2 >= 0:
                return x_change 
            else: 
                return 0 
            
        else:
            return 0
            
     
    def y_move(self,y_change, y_center):

        if y_change > 0: 
                
            if y_center + self.height/2  <= self.y_boundary: 
                return y_change
            else: 
                return 0
                
        elif y_change < 0: 
            if y_center - self.height/2 >= 0:
                return y_change 
            else: 
                return 0 
                
        else:
            return 0





#This class has a methos that scrolls the background, it plots 2 copies of a picture 2 times
#and moves the images at the same time, so it seems like a continous.
class Background: 
    
    def __init__(self,image,screen,screen_w,screen_l): 
        
        self.image = image     
        self.screen = screen
        self.screen_w = screen_w 
        self.screen_l = screen_l
        
    
        self.bg_rectangle = self.image.get_rect()

        self.speed = 1
        self.x_pos = 0
    
        
    def scroll(self):
        
        if self.x_pos < self.screen_w:
            self.x_pos += self.speed         
        else: 
            self.x_pos = 0
                       
        self.screen.blit(self.image,(self.x_pos,0))
        self.screen.blit(self.image, (self.x_pos - self.bg_rectangle.right,0))
        
        
        
        