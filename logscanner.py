# ThisCodedBox Terraria notifier python script
# last modified 26-MAY-2017

# time for pauses
# smtplib for notifications
# random to add that random string

import time
import smtplib
import random, string

#setup the random, random, random maker
def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

# Reset the variables (maybe not needed)

oldAmountOfLines = 0
numNewLines = 0
emailNoFlood = 0

# Pull initial figures, set this to the default
# configuration to prevent false positives on server
# resarts where the file wasn't deleted and was appended
# or when the python script starts after server start
# basically, we don't want it trying to send emails for
# all previous join events on startup

fileHandle = open ( r"c:\tshock\logs\tlivelog.txt" )
lineList = fileHandle.readlines()
fileHandle.close()

# Set the balance at zero to start so it doesn't go back in time

oldAmountOfLines = len(lineList)


print "Ready and waiting for Joins..."

# loop it forever and ever, truth is forever.
while True:
	# don't let email flood variable get too low
	# just in case the number gets OOC
	if emailNoFlood < 0:
		emailNoFlood = 0 
	
	# Pull the log file, get the lines
	fileHandle = open ( r"c:\tshock\logs\tlivelog.txt" )
	lineList = fileHandle.readlines()
	fileHandle.close()
	
	# make variable that that contains how many new lines there are
	
	numNewLines = (len(lineList) - oldAmountOfLines)
	
	# loop through the new lines to search for joins
	# keep in mind this won't even run if there are
	# no new lines so that is pretty efficient
	while numNewLines > 0:
		
		# now grab the first new log line (string) as lineItem
		lineItem = lineList[len(lineList) - (numNewLines) ]
		
		# check for "has joined." text
		if "has joined." in lineItem:
			# if it's there, print the line, and begin the email
			# process provided you haven't sent an email in an
			# 30m or so (1800 seconds, see counter at end)
			print lineList[len(lineList) - (numNewLines) ]
			if emailNoFlood < 1:
				print "EMAIL(s) TO BE SENT"
		
				fromaddr = 'terraria@beyondspec.org'
				toaddrs  = 'daniel.landberg@gmail.com','walrusx4@yahoo.com','sballiet@gmail.com','tim.urian@gmail.com'
				
				# All of this email is boilerplate, save for the 
				# "randomword" which prevents threading on gmail 
				# et al by adding a random string to the subject line
				msg = 'From: terraria@beyondspec.org\nSubject:'+lineItem+'    Notification:['+randomword(10)+']\n\n'+lineItem
				
				user = 'brootlyy'
				password = 'SF8@89dASlF]AS92*@)1'
		
				server = smtplib.SMTP_SSL('server234.web-hosting.com:465')  
				server.login(user,password)
		
				server.sendmail(fromaddr, toaddrs, msg)
		
				server.quit()
		
				print "and ... SENT!" 
				
				# OK, IF you sent an email, don't send one for 30 minutes now
				# important to not set this to 1800 if no email was sent,
				# hence the else statement and this remains in the if statement.
				emailNoFlood = 1800
			else:
				print "***Email sent less than 30m ago, no email sent***"
		# we're back in the original while statement, sequence the numNewLines
		# down one, and run it again (or break out if we're through with new lines)
		numNewLines -= 1
		# maybe this doesn't need to be in the while loop, not sure, but it works.
		oldAmountOfLines = len(lineList)
		
	# The sleep command allows this to cycle approximately once per
	# second, so subtrack 1 from the emailNoFlood variable every time
	# it runs through to allow it to countdown.
	emailNoFlood -= 1
	time.sleep(1)
