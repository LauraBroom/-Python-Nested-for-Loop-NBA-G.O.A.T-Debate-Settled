# All iterations of the inner loop are finished per 1 iteration of the outer loop


player = input("Who is the greatest player of all time: ")

rings = int(input("How many rings does this player have?: "))
# Rings represent rows in our program

seasons = int(input("How many seasons has the player played?: "))
# Seasons represent columns in our program

GoatScore = rings * seasons

#GoatScore is the product of the player's total seasons * total rings
#This is why nested for loops often have a time complexity of O(n^2) 


for i in range (rings):
	for j in range(seasons):
		print(player, end="")
	print()

# end="" After executing a print statement this will prevent our cursor from moving down to the next line
#An empty print statement in Python denotes moving to a new line

print (f"{player} is the Greatest Player of all time. {player}'s G.O.A.T Score is {GoatScore} ")

#F-strings provide a way to embed expressions inside string literals, using a minimal syntax.


#Program moves to a new line after each iteration of the inner loops
#Which means: After the players name has been printed for each season for j amount of Seasons/Columns
#the program moves to a new row per i amount of Rings/Rows
#the G.O.AT Debate is finally settled!!