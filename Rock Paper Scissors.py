#顧名思義，就是寫一個能跟你猜拳的程式啦！
from random import randint

choice = ["rock", "paper", "scissors", "rock", "paper", "scissors"]
def main():
        ai = choice[randint(0,5)] 
        print("Let's play rock paper scissors !! \n")
        while True:
            player = input("Your choice : ")
            
            if player in choice:
                break
            else:
                print("Please enter rock, paper, scissors \n")
                continue

        print("computer choice : " + ai)

        if player == ai:
            print ("Draw\n")

        elif player == "rock" and ai == "paper":
            print ("Computer Wins ! \n")
        elif player == "rock" and ai == "scissors":
            print ("Player Wins ! \n")
        elif player == "paper" and ai == "rock":
            print ("Player Wins ! \n")
        elif player == "paper" and ai == "scissors":
            print ("Computer Wins ! \n")
        elif player == "scissors" and ai == "paper":
            print ("Player Wins ! \n")
        elif player == "scissors" and ai == "rock":
            print ("Computer Wins ! \n")
        
        main()
main()    