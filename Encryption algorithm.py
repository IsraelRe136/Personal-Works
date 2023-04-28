'''
Title: Caesar's cipher
Author: Miguel Angel Verdi Resendiz, verdi.resendiz.miguel@gmail.com
Description:  I decided to implement it using classes (just for practicing), 
if a character of the message is not in the list it returns an error and stops the program, 
as a plus I added the decryption method in the same class.
'''

MESSAGE = "do not eat all my oranges"
TABLE = 'abcdefghijklmnopqrstuvwxyz ' # see the space at the end
KEY = 1


class caesar:
    
    def __init__(self, message,table,key):  
        self.message = message
        self.table = table 
        self.key = key 
    
    #Splits the array of "TABLE" in a dictionary character:position
    def string_to_dictionary(self,string):
        return {item:index for index,item in  enumerate(tuple(string))}

    #This function takes an string, and based on a table of caracteres, 
    #returns a vector with the position of the caracter at the table. 
    def string_to_array(self,string,table_):
        
        message_array = [item for item in tuple(string)]
        message_array_position = []
        
        for caracter in message_array:     
            if caracter in table_: 
                message_array_position.append(table_[caracter])
            else: 
                raise Exception(f"Character {caracter} not found in table :( ")
                
            
        return message_array_position
    
    #This function creates an array of characters based on a vector of positions 
    def position_to_array(self,position_array_,dictionary_): 
        new_array = ''
        
        for position in position_array_:     
            new_caracter = dictionary_[position]
            new_array += new_caracter
        
        return new_array
    
    def encrypt(self): 
        
    
        #Creates a dictionary in the form character:position
        Table_dictionary = self.string_to_dictionary(self.table)
        
        #Creates an array of the positions in the dictionary of each character of the message
        Message_array_position = self.string_to_array(self.message, Table_dictionary)
        
        
        
        #Main encryptation algorithm, changes the positions of every character.
        #It follos New_position = (old_position - key)mod(length of the table)
        for caracter_ in Table_dictionary.keys(): 
            Table_dictionary[caracter_] = (Table_dictionary[caracter_] - self.key)%len(tuple(self.table))
        
    
        
        #Based in the encryptation, creates a dictionary but in the form position:character
        Encrypted_dictionary = {}
        for item,index in Table_dictionary.items(): 
            Encrypted_dictionary[index] = item
        
        
        encrypted_message = self.position_to_array(Message_array_position,Encrypted_dictionary)
        
        
        
        return encrypted_message
        
    def decrypt(self): 
        
    
        #Creates a dictionary in the form character:position
        Table_dictionary = self.string_to_dictionary(self.table)
        
        #Creates an array of the positions in the dictionary of each character of the message
        Message_array_position = self.string_to_array(self.message, Table_dictionary)
        
        
        
        #Main decryptation algorithm, changes the positions of every character.
        #It follos New_position = (old_position + key)mod(length of the table)
        for caracter_ in Table_dictionary.keys(): 
            Table_dictionary[caracter_] = (Table_dictionary[caracter_] + self.key)%len(tuple(self.table))
        
        
        
        #Based in the decryptation, creates a dictionary but in the form position:character
        decrypted_dictionary = {}
        for item,index in Table_dictionary.items(): 
            decrypted_dictionary[index] = item
        
        
        decrypted_message = self.position_to_array(Message_array_position,decrypted_dictionary)
        
        
        return decrypted_message


encryption1 = caesar(MESSAGE,TABLE,KEY)
new_message = encryption1.encrypt()

print(f"Your encrypted message: {new_message}")


decryption1 = caesar(new_message,TABLE,KEY)
original_message = decryption1.decrypt()
print(f"Your original message: {original_message}")










