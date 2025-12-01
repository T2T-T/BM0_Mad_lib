User = int(input("what story would you want to read out of the 3, either 3 little pigs, the big bean stock, and run like lightning. "))
if User == 1:
	print("good choice, here is the stroy, a big bad wolf walks to these 3 houses and says hey im hungry lets go get sum pigs, then he walks to the house and then blows down 2 out of the 3 hosues and the brick house live and the pigs live  ")
elif User == 2: 
	print(" another great choice, he is the story for this, A boy name billy plants a bean stock and then its gets big then it has a house and giants on top")
elif User == 3: print("amazing choice, here is the story, a turtle races a bunny and when the race starts the turtle changes positions with another turtle that looks identical to him at the finish line and beat the bunny and the turtle wins.")

repeat = input("Do you want to read another book? (yes/no):").lower()
if repeat != 'yes':
   print("Exiting liberary. Goodbye!")
   break  # Exit the while loop