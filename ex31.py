print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheesecake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off."
	elif bear == "2":
		print "The bear eats your legs off."
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into an endless abyss."
	print "1. Nonsense."
	print "2. Nonsense."
	print "3. More nonsense."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello."
	else:
		print "The insanity rots your eyes into a pool of muck."

else:
	print "You stumble around and fall on a knife and die."
	
