def numbersWhile(n, m): 
	i = 0
	numbers = []

	#while i < n:
	#	print "At the top i is %d" % i
	#	numbers.append(i)
	#	i = i + m
	#	print "Numbers now: ", numbers
	#	print "At the bottom i is %d" % i
	
	for i in range(n):
		print "At the top i is %d" % i
		numbers.append(i)
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "

	for num in numbers:
		print num

numbersWhile(6, 2)
