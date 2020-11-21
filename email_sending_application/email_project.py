# email project

#  MIME :- Multipurpose Internet Mail Extension
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

message = MIMEMultipart() # create an object of this class
message["Subject"] = "MYNTRA FLAT 50% OFF"
messgae["From"] = "MYNTRA SUMMER SALE"


# sender and receiver
sender = "uttam.saxena5@gmail.com"
receiver = ["meetuttamsaxena@gmail.com","abc@gmail.com"]

# username and password
username = sender
password = open("pwd.txt").read()

# mail body --> in html format

body = """
<h1> MYNTRA FLAT 50% OFF </h1>
<h2> BUY 1 GET 5 FREE </h2>
<h3> SUMMER SALE !! LAST 2 DAYS !! </h3>
"""
txt = MIMEText(body,"html")  #'plain' for simple string
message.attach(txt)

# attach an image
i = open("abc.jpg","rb") # rb -> read binary mode
img = MIMEImage(i.read())
message.attach(img)


server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
print("Connected with the server")

server.login(username,password)
server.sendmail(sender,receiver,message.as_string())
print("Mail Sent Successfully")

























