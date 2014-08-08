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

xmlFile = open("Z:\partners\%s\\request_%s_sf%s\ZI_%s_PersonMatch.xml" % (newfolder, currentDate, newfolder2, newfolder), "w")	


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
	client_name = raw_input("What is the client name? no spaces: ")
	xmlFile.write("    <bean id=\"clientName\" class=\"java.lang.String\">\n")
	xmlFile.write("        <constructor-arg value=\"%s\"/> <!-- Customer NAME NO Date, NO SPACES -->\n" % client_name) 
	xmlFile.write("    </bean>\n")

#creates outputFolder bean.	
def outputFolder():
	xmlFile.write("    <bean id=\"outputFolder\" class=\"java.lang.String\">\n")
	xmlFile.write("        <constructor-arg value=\"%s\"/> <!--FOLDER TO PUT OUTPUT FILE the FILE will be named automatically with Job name Client name and date -->\n" % newpath2) 
	xmlFile.write("    </bean>\n")

#creates personMatcher bean.
def personMatcher():
	inputFile = raw_input("What is the name of the input CSV file (without extension)? ")
	xmlFile.write("    <bean id=\"personMatcher\" class=\"com.zoominfo.component.dsConfig.PersonMatcherConfig\">")
	xmlFile.write("        <property name=\"inputDataFiles\">")
	xmlFile.write("            <list>")
	xmlFile.write("                <bean id=\"personMatchDataFile\" class=\"com.zoominfo.component.dsConfig.InputDataFileConfig\">")
	xmlFile.write("                    <property name=\"filePath\" value=\"c:\partners\%s\request_%s_sf%s\%s.csv\"/> <!-- path to input company file name -->" % (newfolder, currentDate, newfolder2, inputFile)) 
	xmlFile.write("                    <property name=\"hasHeader\" value=\"true\"/>")
	xmlFile.write("                </bean>")
	xmlFile.write("            </list>")
	xmlFile.write("        </property>")
	xmlFile.write("        <property name=\"columnMappings\">")
	xmlFile.write("            <map>")
	coNameKey = raw_input("Please enter the index of the company name column from the input file: ")
	xmlFile.write()
	xmlFile.write()
	xmlFile.write()
	xmlFile.write()
	xmlFile.write()
	
xmlHeader()
jobName()
clientName()
outputFolder()

"""
while True:	
	try: 
		firstKey = int(coNameKey)
	except ValueError:
		print "This is not an integer. Please try again."
		
	xmlFile.write("			<entry key=\"%d\" value=\"personresumecompanyname\" />") % firstKey
	xmlFile.write("")
	xmlFile.write("")
"""