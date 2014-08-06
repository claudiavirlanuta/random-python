import os, sys
import time
import datetime

#prompts user for new client folder name
newfolder = raw_input("Please enter a name for the client directory: > ")

#creates the path for the new folder
newpath = r'Z:\partners\%s' % newfolder

#get current date in m_d_t format
currentDate = datetime.datetime.now().strftime("%m_%d_%y")

if not os.path.exists(newpath):
	os.makedirs(newpath)

newfolder2 = raw_input("Please enter the SFDC case number: > ")

newpath2 = r'Z:\partners\%s\request_%s_sf%s' % (newfolder, currentDate, newfolder2)

if not os.path.exists(newpath2):
	os.makedirs(newpath2)

xmlFile = open("Z:\partners\%s\request_%s_sf%s\ZI_%s_CompanyMatch.xml", "w") % newfolder
