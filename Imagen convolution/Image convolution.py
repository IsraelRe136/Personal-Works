import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np 



"""
Title:  Image convolution
Author: Miguel Angel Verdi Resendiz, verdi.resendiz.miguel@gmail.com
Description:  This is an algorithm that takes an RBG image in format jpg, 
and a kernel nxn and makes a convolution usign 
"""



class Convolution:
    

    
    def __init__(self,img_): 
        
        self.Img = img_
        
      
    
    def Filter(self,kernel): 
        
        #Firts we have to check if the kernel is valid, is a method constructed above
        if self.Check(kernel,self.Img):
            
            #Get the lenght of the picture, so we can iterate

            img_h, img_w, img_d = np.shape(self.Img)
            kernel_h, kernel_w = kernel.shape
            
            
            
            #Cut the image for making the kernel product
            cut_img = np.zeros((img_h + (kernel_h//2)*2 +2, img_w + (kernel_w//2)*2 +2, img_d))
            cut_img[(kernel_h//2):-kernel_h, (kernel_w//2):-kernel_w, :] = img

            #Create an empty plot.
            new_img = np.zeros_like(img)
            
            
            
            #Here we are moving through the picture first by column, then by row, then by dimension
            for row_iterable in range(img_h):
                for column_iterable in range(img_w):  
                    for dim in range(img_d):
                        
                        new_img[row_iterable, column_iterable, dim] = np.sum(cut_img[row_iterable:row_iterable+kernel_h, 
                                                                                     column_iterable:column_iterable+kernel_w, 
                                                                                     dim] * kernel)
                
                
                    
    
            return new_img
        
        
        else:
            print("Invalid parameters of Kernel")
            return False
        
        

    def Check(self,kernel_, Img_): 
        
        #Check should be true so we can convulate,
        #Kernel should be dimension bigger than 0, an squarem and smaler than picture.
        check = True 
        check = check if np.shape(kernel_) > (0,0) else False
        check = check if np.shape(kernel_)[1] == np.shape(kernel_)[0]  else False
        check = check if np.shape(kernel_) <= np.shape(Img_) else False
        
        return check 
        
    def Show(self):
    
        plt.imshow(self.Img)
        
        
        
   
if __name__ == '__main__':        
    
    #Inpunt parameters.
    get_image = mpimg.imread('Cardenal.jpg')
    Kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    
    
    
    
    
    #Creating the objet of convolution image
    img = get_image.copy()    
    img_convolution = Convolution(img) 
    new_image = img_convolution.Filter(Kernel)
    
    
    
    
    fig, (ax1,ax2) = plt.subplots(nrows = 1, ncols = 2) 
    ax1.imshow(get_image)
    ax2.imshow(new_image) 
    
    ax1.set_title("Original Image", fontsize=20)
    ax1.set_xlabel("x") 
    ax1.set_ylabel("y") 
    
    ax2.set_title("Processed image", fontsize=20)
    ax2.set_xlabel("x") 
    ax2.set_ylabel("y")
    plt.subplots_adjust(hspace=0, wspace=0.5)
    
    
    plt.show()





