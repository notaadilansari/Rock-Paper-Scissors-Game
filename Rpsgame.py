#rock paper scissor game
#importing random for fair choice of computer
import random
#defining rpsgame class


class rpsgame:
	
  
  #storing name
	def __init__(self,name):
		self.name=name
		self.player_score=0
		self.computer_score =0
	
  
  #playing game
	def play_round(self):
		
    
    #taking player choice
		player_choice=input("Enter your move (rock/paper/scissor) : ")
		l1=["rock","paper","scissor"]
		random_sample=random.randint(0,2)
		computer_choice=l1[random_sample]
		print(f"Compter Choice : {computer_choice}")
		
    
    #using conditional expression for result
		if player_choice==computer_choice:
			print("Result : draw")
		elif player_choice=="rock" and computer_choice=="paper":
			print("Result : You lose")
			self.computer_score+=1
		elif player_choice=="rock" and computer_choice=="scissor":
			print("Result : You Win")
			self.player_score+=1
		elif player_choice=="paper" and computer_choice=="rock":
			print("Result : You win")
			self.player_score+=1
		elif player_choice=="paper" and computer_choice=="scissor":
			print("Result : You lose")
			self.computer_player+=1
		elif player_choice=="scissor" and computer_choice=="paper":
			print("Result : You lose")
			self.player_score+=1
		elif player_choice not in l1:
			print("invalid choice \n choose again \n")
			self.play_round()
		else:
			print("Result : You lose")
			self.computer_score+=1
  
  
  #showing score using show_score method
	def show_score(self):
		print("---SCOREBOARD---")
		print(f"{self.name} : {self.player_score}")
		print(f"Computer : {self.computer_score}")
name=input("Enter Player Name: ")
round=int(input("Enter number of round : "))
print("\n")
player=rpsgame(name)
for i in range(0,round):
	player.play_round()
	print("\n")
player.show_score()
