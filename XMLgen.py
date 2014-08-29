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
client_name = raw_input("What is the client name? no spaces: ")
xmlFile = open("Z:\partners\%s\\request_%s_sf%s\ZI_%s_PersonMatch.xml" % (newfolder, currentDate, newfolder2, client_name), "w")	


# creates xml file header, which points to the location of the schema.
def xmlHeader():
	xmlFile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
	xmlFile.write("<beans xmlns=\"http://www.springframework.org/schema/beans\"\n")
	xmlFile.write("       xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\n")
	xmlFile.write("       xmlns:context=\"http://www.springframework.org/schema/context\"\n")
	xmlFile.write("       xmlns:lang=\"http://www.springframework.org/schema/lang\"\n")
	xmlFile.write("       xmlns:util=\"http://www.springframework.org/schema/util\"\n")
	xmlFile.write("\n")
	xmlFile.write("       xsi:schemaLocation=\"http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-2.5.xsd \n")
	xmlFile.write("          http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-2.5.xsd \n")
	xmlFile.write("          http://www.springframework.org/schema/lang http://www.springframework.org/schema/lang/spring-lang-2.5.xsd \n")
	xmlFile.write("          http://www.springframework.org/schema/util http://www.springframework.org/schema/util/spring-util-2.5.xsd \n")
	xmlFile.write("          http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop-2.5.xsd\" \n")
	xmlFile.write("          default-autowire=\"no\"\n")
	xmlFile.write("          default-lazy-init=\"true\" xmlns:aop=\"http://www.springframework.org/schema/aop\">\n")
	xmlFile.write("\n")

# creates jobName bean.
def jobName():
	job_name = raw_input("What is the job name? no spaces: ")
	xmlFile.write("    <bean id=\"jobName\" class=\"java.lang.String\">\n")
	xmlFile.write("        <constructor-arg value=\"%s\"/> <!-- LISTTYPE_(Titles) NO Date, NO SPACES-->\n" % job_name) 
	xmlFile.write("    </bean>\n")

# creates clientName bean.	
def clientName():
	
	xmlFile.write("    <bean id=\"clientName\" class=\"java.lang.String\">\n")
	xmlFile.write("        <constructor-arg value=\"%s\"/> <!-- Customer NAME NO Date, NO SPACES -->\n" % client_name) 
	xmlFile.write("    </bean>\n")

#creates outputFolder bean.	
def outputFolder():
	xmlFile.write("    <bean id=\"outputFolder\" class=\"java.lang.String\">\n")
	np_string = str(newpath2)
	s = list(np_string)
	s[0] = 'C'
	np_string = "".join(s)
	xmlFile.write("        <constructor-arg value=\"%s\"/> <!--FOLDER TO PUT OUTPUT FILE the FILE will be named automatically with Job name Client name and date -->\n" % np_string) 
	print np_string
	xmlFile.write("    </bean>\n")

#creates personMatcher bean.
def personMatcher():
	inputFile = raw_input("What is the name of the input CSV file (without extension)? ")
	xmlFile.write("    <bean id=\"personMatcher\" class=\"com.zoominfo.component.dsConfig.PersonMatcherConfig\">\n")
	xmlFile.write("        <property name=\"inputDataFiles\">\n")
	xmlFile.write("            <list>\n")
	xmlFile.write("                <bean id=\"personMatchDataFile\" class=\"com.zoominfo.component.dsConfig.InputDataFileConfig\">\n")
	xmlFile.write("                    <property name=\"filePath\" value=\"c:\partners\%s\\request_%s_sf%s\%s.csv\"/> <!-- path to input company file name -->\n" % (newfolder, currentDate, newfolder2, inputFile)) 
	xmlFile.write("                    <property name=\"hasHeader\" value=\"true\"/>\n")
	xmlFile.write("                </bean>\n")
	xmlFile.write("            </list>\n")
	xmlFile.write("        </property>\n")
	xmlFile.write("        <property name=\"columnMappings\">\n")
	xmlFile.write("            <map>\n")
	email = raw_input("Does the input file contain emails? Y/N: ")
	#Can only match to Email or Email+CompName+FN+LN, or CompName+FN+LN.
	#If not email in input file, match to CompName+FN+LN.
	if email == "n" or email == "N":
		Co_FN_LN()	
	#Write email column params when emails exist.
	elif email == "y" or email == "Y": 
		emailKey = raw_input("Please enter the Email column index: ")
		fourthKey = int(emailKey)
		xmlFile.write("			<entry key=\"%d\" value=\"email1\" />\n" % fourthKey)
		moreInfo = raw_input("Does the input file contain Company Name, First Name AND Last Name? Y/N: ")
		#If input contains Co_FN_LN as well, those params are also written to the XML.
		if moreInfo == "y" or moreInfo == "Y":
			Co_FN_LN()
		else: 
			print "The match will be based solely on email."
		
	else:
		print "You cannot do a person match on the current input file."
	xmlFile.write("\n            </map>\n")
	xmlFile.write("        </property>\n")
	xmlFile.write("    </bean>\n")
	xmlFile.write("</beans>")


def Co_FN_LN():
	coNameKey = raw_input("Please enter the Company Name column index: ")
	firstKey = int(coNameKey)
	xmlFile.write("			<entry key=\"%d\" value=\"personresumecompanyname\" />\n" % firstKey)
	firstNameKey = raw_input("Please enter the First Name column index: ")
	secondKey = int(firstNameKey)
	xmlFile.write("			<entry key=\"%d\" value=\"firstname\" />\n" % secondKey)
	lastNameKey = raw_input("Please enter the Last Name column index: ")
	thirdKey = int(lastNameKey)
	xmlFile.write("            <entry key=\"%d\" value=\"lastname\" />\n" % thirdKey)

xmlHeader()
jobName()
clientName()
outputFolder()
personMatcher()

"""
while i == True:	
	try: 
		firstKey = int(coNameKey)
		i == False
	except ValueError:
		print "This is not an integer. Please try again."
		i == True
		
	xmlFile.write("			<entry key=\"%d\" value=\"personresumecompanyname\" />") % firstKey
	xmlFile.write("")
	xmlFile.write("")
"""