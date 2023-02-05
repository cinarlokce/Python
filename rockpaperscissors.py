#RockPaperScissors game

import random
Player1_score=0
Player2_score=0
act_list=["rock","paper","scissors"]
round=0
rounds=int(input("How many rounds do you want to play?"))
while True:
  Player1_choice=random.choice(act_list)
  Player2_choice=random.choice(act_list)
  print("\nPlayer1: "+Player1_choice+"\nPlayer2: "+Player2_choice)
  if Player1_choice=="paper":
    if Player2_choice=="paper":
      print("Tie! Both players chose the same action")
    elif Player2_choice=="rock":
      print("Player1 won the round")
      Player1_score+=1
    elif Player2_choice=="scissors":
      print("Player2 won the round")
      Player2_score+=1

  if Player1_choice=="rock":
    if Player2_choice=="rock":
      print("Tie! Both players chose the same action")
    elif Player2_choice=="scissors":
      print("Player1 won the round")
      Player1_score+=1
    elif Player2_choice=="paper":
      print("Player2 won the round")
      Player2_score+=1

  if Player1_choice=="scissors":
    if Player2_choice=="scissors":
      print("Tie! Both players chose the same action")
    elif Player2_choice=="paper":
      print("Player1 won the round")
      Player1_score+=1
    elif Player2_choice=="rock":
      print("Player2 won the round")
      Player2_score+=1
  round+=1

  if round>=rounds:
    k=input("Do you want to continue to play the game(Yes/No): ")
    if k=="Yes":
      continue
    else:
      break

print("\n\nPlayer1's score: "+str(Player1_score)+"\nPlayer2's score: "+str(Player2_score))
