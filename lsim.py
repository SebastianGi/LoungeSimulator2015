#!/usr/bin/env python3.5

import random

teams = []
money = 5.00

moneymade = 0
moneylost = 0
highscore = 0

team1 = ""
team2 = ""
chance1wins = 0
chance2wins = 0
saltedchance1wins = 0
saltedchance2wins = 0
salt = ""
currbet = 0
mult1 = 0
mult2 = 0

tempinput = ""



def initTeams():
	teams.append("Ninjas in Tanktops")
	teams.append("Mett Catz")
	teams.append("IchKaufeKraft")
	teams.append("Team BRushDontStop")
	teams.append("Wolke9")
	teams.append("Team Pinguin")
	teams.append("Team Solid")
	teams.append("22Ti")
	teams.append("Team Vulnerable")
	teams.append("Team UMP")
	teams.append("Pro90Rush")
	teams.append("Virus Brot")
	teams.append("Team Brony")
	teams.append("Fapnatic")
	teams.append("Germany")
	teams.append("Poland")
	teams.append("USA")
	teams.append("Sweden")
	teams.append("Russia")
	teams.append("Mothers of Russia")
	teams.append("Sloppy Seconds")
	teams.append("Team Bratmaxe")
	teams.append("L33tH4x0R5")
	teams.append("Volvo")
	teams.append("Meaty")
	teams.append("Team GreyFace")
	teams.append("Autonoobs")

def newRound():
	#Getting Teams for Round
	global team1
	global team2
	team1 = teams[random.randint(0, len(teams)-1)]
	while True:
		team2 = teams[random.randint(0, len(teams)-1)]
		if team2 != team1:
			break
	print(team1, team2)
	
	#Getting popability that team 1 wins
	chance1wins = random.randint(5, 95)
	chance2wins = 100 - chance1wins
	
	#Generating salt(emulating other betters so we can calculate money made/lost)
	#Is currently +/-15, but can be changed to make betting harder/easier
	while True:
		salt = random.randint(-15,15)
		if (chance1wins + salt) > 2 and (chance1wins + salt) < 98:
			break
	saltedchance1wins = chance1wins + salt
	saltedchance2wins = 100 - saltedchance1wins
	print(chance1wins, chance2wins, salt, saltedchance1wins, saltedchance2wins)
	
	#Calculating the potential win (1*loserodds/winnerodds*0.97)
	#the 0.97 are the share the casino gets from every bet
	#variables are the multiplicator that gets applied to the bet
	mult1 = 1 * saltedchance2wins / saltedchance1wins * 0.97
	mult2 = 1 * saltedchance1wins / saltedchance2wins * 0.97
	print(round(mult1, 2), round(mult2, 2))
	

def grabMoneyInput():
	print("\nHow much do you want to bet?\n")
	while True:
		try:
			global currbet
			currbet = int(input())
			if currbet > money:
				print("You don't have that much money\n")
			elif currbet < 0.01:
				print("You didn't bet any money\n")
			else:
				break
		except ValueError:
			print("Input not a Number\n")

def team1bet():
	grabMoneyInput()
	global money
	global currbet
	money = money - currbet
	#Won
	if simgame(chance1wins, team1, team2) == True:
		global moneymade
		global money
		money = money + currbet
		currbet = round(currbet * mult1, 2) #switch
		money = money + currbet
		moneymade = moneymade + currbet
		
		print("You won the bet and made", currbet)
	#Lost
	else:
		global moneylost
		moneylost = moneylost + currbet
		print("You lost the bet")
	pass
		

def team2bet():
	grabMoneyInput()
	money = money - currbet
	#Won
	if simgame(chance1wins, team1, team2) == False:
		pass
	#Lost
	pass

#Simulating a game and returning the winner as a bool(True= Team1, False= Team2)
def simgame(chance1, team1, team2):
	win1 = 0
	i1 = 0
	i2 = 0
	w1 = 0
	w2 = 0
	playedround = 0
	gamerounds = []
	#To decide who wins Game
	temp = random.randint(1, 100)
	#To decide how many Rounds each team won
	temp2 = random.randint(0, 15)
	if temp > chance1:
		win1 = False
		i2 = 16
		i1 = round(((chance1)/10) + temp2)
		if i1 > 15:
			i1 = 15
	else:
		win1 = True
		i1 = 16
		i2 = round(((100-chance1)/10) + temp2)
		if i2 > 15:
			i2 = 15
	for i in range(i1):
		gamerounds.append(1)
	for i in range(i2):
		gamerounds.append(2)
	random.shuffle(gamerounds)
	for i in range(len(gamerounds)):
		if gamerounds[i] == 1:
			w1 = w1 + 1
			playedround = playedround + 1
			print("Round", playedround, ": ", team1, "won their", w1, " round.")
		else:
			w2 = w2 + 1
			playedround = playedround + 1
			print("Round", playedround, ": ", team2, "won their", w2, " round.")
		if w1 == 16:
			return True
		if w2 == 16:
			return False

initTeams()
print("\nTeams:\n" , teams)

#Looping for every Round until no money left
while money > 0.01:
	newRound()
	tempinput = ""
	#Accepting Input for Team
	while True:
		tempinput = input("\nPlease enter which team you want to bet on:\n")
		if tempinput == "0" or tempinput == "":
			break
		elif tempinput == "1" or tempinput == team1:
			team1bet()
			break
		elif tempinput == "2" or tempinput == team2:
			team1bet()
			break

print("No money left, ending game")
quit()