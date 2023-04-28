import random 

"""
Title:  Rock, paper, scissors
Author: Miguel Angel Verdi Resendiz, verdi.resendiz.miguel@gmail.com
Description:  This is an algorithm that gives the results of the simulation of a them game 
Rock,paper,scissors. 
"""



class Player:
   
    # constructor
    def __init__(self,**kwargs):
        self.player_probabilities = kwargs    
    
    # validity_check
    def validity_check(self):
        
        #Fist condition sum of all probabilities  = 1. 
        conditions = True if sum(self.player_probabilities.values()) == 1 else False
        
        #Condition that each probabilitie sould be 0 <= P <= 1. 
        for value in self.player_probabilities.values():
            
            conditions = conditions if value >= 0 and value <= 1 else False 
            
        return conditions
            

    def __repr__(self):
        
        print(f"Probabilities of the player: {self.player_probabilities}")
        
        

    pass



class Game:
    
    # constructor
    def __init__(self,Number_of_rounds,
                 Player_a_Probabilities, Player_a_validity_check,
                 Player_b_Probabilities, Player_b_validity_check):
        
        self.Number_of_rounds = Number_of_rounds
        self.Player_a_Probabilities = Player_a_Probabilities
        self.Player_a_validity_check = Player_a_validity_check
        self.Player_b_Probabilities = Player_b_Probabilities
        self.Player_b_validity_check = Player_b_validity_check
        
         
        
    # validity_check
    def validity_check(self): 
        #Condition for numer of rounds > 0
        validity = True if self.Number_of_rounds > 0 else False
        
        #Condition for both validities of players should be True
        validity = validity if self.Player_a_validity_check and self.Player_b_validity_check else False
        
        return validity
    
    
        
    # run_game
    def run_game(self): 
        
        if self.validity_check() == True: 
            
            #Dictionary of results, will be fill at the end
            Results = {'player_a': 0,
                       'player_b': 0,  
                       'tie': 0,
                       }
            
            
            for game in range(self.Number_of_rounds):
                
                #We create a variable that is random between [0,1]
                prob_player_a = random.uniform(0, 1)
                prob_player_b = random.uniform(0, 1)
                
                #Now, for taking in count the stategy of each player, 
                #we divide the range [0,1] in 3 sections based of the probability of each movement,
                #So with this, the random variable has diferent probabilities to be in each section.
                
                player_a_move = ""
                
                if prob_player_a < self.Player_a_Probabilities['scissors']:
                    player_a_move = 'S'
                elif self.Player_a_Probabilities['scissors'] < prob_player_a and prob_player_a < self.Player_a_Probabilities['scissors'] + self.Player_a_Probabilities['paper'] :
                    player_a_move = 'P'
                else: 
                    player_a_move = 'R'
                    
                player_b_move = ""
                
                if prob_player_b < self.Player_b_Probabilities['scissors']:
                    player_b_move = 'S'
                elif self.Player_b_Probabilities['scissors'] < prob_player_b and prob_player_b < self.Player_b_Probabilities['scissors'] + self.Player_b_Probabilities['paper'] :
                    player_b_move = 'P'
                else: 
                    player_b_move = 'R'
                
                
                #We call a function that based in each playe's desition of movent, returns a winner
                Winner = self.game_winner(player_a_move,player_b_move)
                
                
                #The funcion game_winner returns A for player A winner, B for player B winner or T for tie.
                #So depending of who was the winner in this round, it sums at dictionary of results
                if Winner == 'A': 
                    Results['player_a'] += 1
                elif Winner == 'B': 
                    Results['player_b'] += 1
                else:
                    Results['tie'] += 1
                
                
            return Results
                
        else:
            print("Game aborted")
            return False
        
    #Function that chose a winner based on the rules and on each player's move.
    def game_winner(self,*args):
        
        #The rules, example if player a chosses S(scissors) and player b chosses P (paper), the winner would be player A. 
        Rules =  {('S','P') : 'A', ('S','R') : 'B', ('S','S') : 'T',
                  ('P','S') : 'B', ('P','R') : 'A', ('P','P') : 'T',
                  ('R','S') : 'A', ('R','P') : 'B', ('R','R') : 'T'}
        
        
        Player_a_move, Player_b_move = args
        winner  = Rules[Player_a_move, Player_b_move]
        
        
        return winner
            
            
            
            
    # get_results
    def get_results(self,Results):
        
        if Results != False: 
            return Results
        else: 
            return False
        
    def __repr__(self): 
        print(f"Number of rounds for this game {self.Numer_of_rounds} ")
        print(f"Player a  probabilities: {self.Player_a_Probabilities}, Validation: {self.Player_a_validity_check}")
        print(f"Player b  probabilities: {self.Player_b_Probabilities}, Validation: {self.Player_b_validity_check}")
     
    pass




def rock_paper_scissors(number_of_rounds, player_a, player_b):

    # create player_a
    Player_a = Player(**player_a)
   
    # create player_b
    Player_b = Player(**player_b)
    # create game    
    new_game = Game(number_of_rounds,
                    Player_a.player_probabilities, Player_a.validity_check(),
                    Player_b.player_probabilities, Player_b.validity_check()
                    )
    
    # run game
    Results_of_game = new_game.run_game()       
    
    # get result
    Final_results = new_game.get_results(Results_of_game)
    """ ^^^^ YOUR CODE ENDS HERE ^^^^ """
    #return result
    print(Final_results)
    return Final_results

if __name__ == '__main__':
    
    N = 1000
    PLAYER_A = {
        "paper": 0.8,
        "scissors": 0.1,
        "rock": 0.1,
    }
    PLAYER_B = {
        "paper": 0.1,
        "scissors": 0.8,
        "rock": 0.1,
    }
    rock_paper_scissors(N, PLAYER_A, PLAYER_B)
    # Approximate output: {'player_a': 170, 'player_b': 640, 'tie': 190} (could vary slightly because of the randomness)



    # Test case 2
    N = 100
    PLAYER_A = {
        "paper": 0,
        "scissors": 1,
        "rock": 0,
    }
    PLAYER_B = {
        "paper": 0,
        "scissors": 0,
        "rock": 1,
    }
    assert rock_paper_scissors(N, PLAYER_A, PLAYER_B) == {'player_a': 0, 'player_b': 100, 'tie': 0}


    # Test case 3
    N = 0
    PLAYER_A = {
        "paper": 0,
        "scissors": 1,
        "rock": 0,
    }
    PLAYER_B = {
        "paper": 0,
        "scissors": 0,
        "rock": 1,
    }
    assert rock_paper_scissors(N, PLAYER_A, PLAYER_B) is False
    
    
    
    