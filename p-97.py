number=int("5")
tries=int("1")
answer1=int("2")
answer2=int("2")
answer3=int("2")
# Here I am using answer as a medium to discover if the answer is correct or not, I will ask more questions 
# accordingly. It is 0= no and 1 = yes and 2 is neutral so that I can avoid errors
intro=input("Hi, please give us your name:")
startGame=int(input("Hi" +" "+intro+" "+ "lets start the game! Pick a number from 1-10 :"))

if(tries==0):
    print("Game over, you've lost")

if (startGame==5):
   print("Congrats, you have won the game")

elif (startGame > 5):
    tries-=1
    answer1="0"
    input("Your guess was too high, you have"+" "+str(tries)+" "+"more tries, please try again")
    
else :
    tries-=1
    answer1="0"
    input("Your guess was too low, you have"+" "+str(tries)+" "+"more tries, please try again")


    
