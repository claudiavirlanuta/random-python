from sys import argv

def quoter():
	i = argv
	file = open(str(argv[1]), 'r')
	lines = file.readlines()
	file.close()
	f = str(argv[1])
	o = open('C:\Users\claudia.virlanuta\Documents\%s_quoted.csv' %f, 'w' )
	for j in lines:
		quoted = '"'+str(j).rstrip('\n')+'"'+'\r'
		o.write('%s' %quoted)
	
quoter()
