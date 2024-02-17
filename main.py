import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import base64


smtp_server = "smtp.gmail.com"
smtp_port = 587  
smtp_username = "adhyaaya.gcoen@gmail.com"
smtp_password = "jbeo kvvd eony eokq"



def send_email(subject, body, to_email, image_path, smtp_server, smtp_port, smtp_username, smtp_password):  
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    with open(image_path, 'rb') as image_file:
        image = MIMEImage(image_file.read(), name='reciept.png')
        message.attach(image)
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, message.as_string())



subject = "Confirmation regarding online registeration in Adhyaaya'24"
body = "Dear Participant,\n"+"We are excited to inform you that your registration for the Adhyaaya Technical fest has been confirmed. \nWe are sending you an attachment of your reciept so that we can authenticate you in the event.\n Join us for a fantastic event filled with technical challenges, workshops, and networking opportunities. Have fun! \nBest regards,\nAdhyaaya Technical Team"
to_email = "tanishqbakka1@gmail.com"
image_path = "./Bob.png"  
send_email(subject, body, to_email, image_path, smtp_server, smtp_port, smtp_username, smtp_password)




