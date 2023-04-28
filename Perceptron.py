import numpy as np
import matplotlib.pyplot as plt



class Perceptron: 
    
    def __init__(self, d:int, activation  = 'linear'):
        
        self._weights = np.full((d +1,1), fill_value=0.0)
        
        
        
    def fit(self,x,y):
        """
        

        Parameters
        ----------
        x : Matrix <N,d>.
        y : Vector <N,1>.

        Returns
        -------
        .

        """
        
        alpha = 0.01
        
        
        steps = 30
        
        for step in range(steps): 
            
            #Prepare gradients
            error = self.predict(x) - y  # vector <N,1>
            shape = np.shape(x)
            x_star = np.c_[np.full((shape[0],1),fill_value = 1) ,x ]
            N = shape[0]
        
            dphi_dz =self.activation_function_derivative(x_star @ self._weights)
            
            gradient = (1./N)*np.transpose(np.multiply(error, dphi_dz)) @ x_star 
            
            
            
        
        
        #Update weights
        
            self._weights += -alpha*np.transpose(gradient)
        
        
        
        return error
    
    def predict(self,x):
        
        """
        x - matrix <M,d>
        
        
        Returns
        -------
        vector <M,1>
        
        
        """
        
        shape = np.shape(x)
            
        x_star = np.c_[np.full((shape[0],1),fill_value = 1),x]
        
        
        
        output = self.activation_function(x_star  @ self._weights)
        
        #output = x_star
        
        return output
    
        
    


    def activation_function(self,z): #z = w@x
        
        
        phi = 1/(1 + np.exp(-z))
        return phi
        
        
        
    def activation_function_derivative(self,z):
        
        dphi = self.activation_function(z)*(1- self.activation_function(z))
        
        return dphi
        

if __name__ == '__main__':
    
    
    
    x = np.transpose(np.array(
        [
            
            [20.5,35,40,13.5,7.5,6,15],
            [30,26,20,19,32,30,52]
            ]
        
        
        ))
    
    model = Perceptron(2)
    
    y = np.transpose(np.array([[1,1,1,1,0,0,0]]))
    

    
    model.fit(x,y)
    
    print(model.predict(x))
    
    
       # price = np.array([0,0,0,150., 135., 200., 400., 350., 200.])
    # num_rooms = np.array([0,0,0,1, 1, 2, 5, 3, 3])

    # model = Perceptron(1)        
    
    # num_rooms_text = np.array([0,1,2,3,4,5,6,7])
    
    
    # x = num_rooms.reshape((len(num_rooms),1))
    # y = price.reshape((len(price) , 1))
    # model.fit(x,y)

    # print(model.predict(num_rooms_text))


 
    