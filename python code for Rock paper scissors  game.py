#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint

print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n"
                                +"And check letters are case sensitive \n")



t = ["Rock","Paper","Scissors"]

system = t[randint(0,2)]

player = False


while player == False:
    
    
    player = ("Rock,Paper,Scissors?")
    if player == system:
        print("Tie!")
    elif player == "Rock":
        if system == "Paper":
            print("you lose!")
        else:
            print("you win!")
    elif player == "Paper":
        if system == "Scissors":
            print("you lose!")
        else:
            print("you win!")
    elif player == "Scissors":
        if system == "Rock":
            print("you lose!")
        else:
            print("you win!")
    else:
        print("That's not a valid play. Check your spelling!")
    
        
    #player was set to True, but we want it to be False so the loop continues
    
    player = False
    
    system = t[randint(0,2)]
            
            
    
    

