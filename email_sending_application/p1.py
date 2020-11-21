# email sending application
'''
import smtplib to make a connection with the gmail smtp server
'''

#1) we need to import a library that is smtplib
import smtplib

#2) SMTP --> create an object
'''
1) server address
2) port number
'''
server = smtplib.SMTP("smtp.gmail.com",587)

#3) call starttls() to make a secure connection
server.starttls()

print("connected with the server")

#4) you can login by using login()

server.login("uttam.saxena5@gmail.com",open("pwd.txt").read())

#5) now you can send an email by using sendmail()

server.sendmail("uttam.saxena5@gmail.com","meetuttamsaxena@gmail.com","hello")

print("mail sent successfully")
























