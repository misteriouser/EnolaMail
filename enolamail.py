import smtplib
import sys
import time
import getpass

#Requirements
username = input("Username: ")
password = getpass.getpass("Password: ")
fromaddress = input("From: ")
to = input("To: ")
number = 50

#Start the mail
server = smtplib.SMTP("smtp.gmail.com: 587")
server.ehlo()
server.starttls()
server.login(username, password)

def sendMail():
  server.sendmail(fromaddress, to, str(mail + 1))

# The actual mail send
for mail in range(number):
  sendMail()
  sys.stdout.write("\x1b[2K\r" + str(((mail + 1) * 100) / number) + "%"),
  sys.stdout.flush()
