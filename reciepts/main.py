import csv
import os
import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import base64


smtp_server = "smtp.gmail.com"
smtp_port = 587  
smtp_username = "adhyaaya.gcoen@gmail.com"
smtp_password = "jbeo kvvd eony eokq"
eventName=''
date=''
time=''
event_info = [{
    "eventName": "Cricbash",
    "Date": "20/02/24 & 21/02/24",
    "Time": "Day 1 : 12:30-6:00\nDay 2 : 10:30-6:00 "
},{
    "eventName": "Avishkar",
    "Date":"20/02/24",
    "Time": "12:00-2:00 ",
    
},{
    "eventName": "Lounge",
    "Date": "20/02/24 & 21/02/24",
    "Time": "Day 1 : 2:00-4:30\nDay 2 : 12:00-3:00",
},{
    "eventName": "Virtual Placement",
    "Date": "20/02/24 & 21/02/24",
    "Time": "Day 1 : 11:00-12:00(Paper) \n2:30-5:00(GD)\nDay 2 : 12:00-4:00"
},{
    "eventName": "Foodoholic",
    "Date": "20/02/24 & 21/02/24",
    "Time": "Day 1 : 1:00-6:00\nDay 2 : 1:00-6:00"
},{
    "eventName": "Respawn",
    "Date": "20/02/24",
    "Time": "6:00-Onwards"
},{
    "eventName": "Innovation-Express",
    "Date": "20/02/24",
    "Time": "3:30-5:00",
},{
    "eventName": "Structure-Spy",
    "Date": "21/02/24",
    "Time": "11:00-1:00",
},{
    "eventName": "Stock-Talk",
    "Date": "21/02/24",
    "Time": "12:00-3:00",
},{
    "eventName": "VaadVivaad",
    "Date": "21/02/24",
    "Time": "11:00-6:00",
},{
    "eventName": "Born-Psychos",
    "Date": "21/02/24",
    "Time": "10:30-6:00",
},{
    "eventName": "Codeventure",
    "Date": "21/02/24",
    "Time": "11:00-6:00",
},{
    "eventName": "Roborace",
    "Date": "21/02/24",
    "Time": "11:00-5:00",
},{
    "eventName": "Stargaze",
    "Date": "21/02/24",
    "Time": "5:00-7:30",
},{
    "eventName": "Quiz Master",
    "Date": "22/02/24",
    "Time": "12:00-2:00",
},{
    "eventName": "GDSC TF workshop",
    "Date": "22/02/24",
    "Time": "12:00-2:00",
},{
    "eventName": "Jigyasa",
    "Date": "22/02/24",
    "Time": "Online",
}]

width, height = 640, 240
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

bg_array = []
for i in range(0,25):
    bg_array.append("bg_{}.jpg".format(i))
    
random.shuffle(bg_array)

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


def truncate_string(input_string, max_length):
    if len(input_string) > max_length:
        truncated_string = input_string[:max_length]
        return truncated_string+'...'
    else:
        return input_string
    
folder_path = './csv/'

# Get a list of files in the folder
files = os.listdir(folder_path)

csv_files = [file for file in files if file.endswith('.csv')]

for csv_file in csv_files:
        file_name = os.path.splitext(os.path.basename(csv_file))[0]
        print(file_name)
        output_directory = './' + file_name
        
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
    
        file_path = os.path.join(folder_path, csv_file)
        with open('./csv/'+file_name+'.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                for i in range (0,len(event_info)):
                    if event_info[i].get("eventName")==file_name:
                        date=event_info[i].get("Date")
                        time=event_info[i].get("Time")
                image_to_add_path = bg_array[random.randint(0,len(bg_array)-1)]
                image_to_add = Image.open(image_to_add_path)
                image_to_add = image_to_add.resize((640, 240))
                image_position = (0, 0)
                image.paste(image_to_add, image_position)
                
                image_to_add_path = "solid.png"
                image_to_add = Image.open(image_to_add_path).convert("RGBA")
                image_to_add = image_to_add.resize((150, 112))
                image_position = (480, 120)
                image.paste(image_to_add, image_position, image_to_add)
                
                draw = ImageDraw.Draw(image)
                custom_font_path = "font-2.ttf"
                text = "Participant Details "
                text_color = "gold"
                custom_font = ImageFont.truetype(custom_font_path, 48)
                draw.text((20, 20), text, font=custom_font, fill=text_color)
                
                custom_font_path = "oykobold.ttf"
                text = 'Event Details \nDate : {} \nTime : {}'.format(date,time)
                text_color = "white"
                custom_font = ImageFont.truetype(custom_font_path, 10)
                draw.text((410, 35), text, font=custom_font, fill=text_color)
                
                #qr starts
                
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=2.2,
                    border=2,
                )
                qr.add_data("https://qr-authenticate.vercel.app/?email={}&event={}".format(row[2],str(file_name)))
                print("https://qr-authenticate.vercel.app/?email={}&event={}".format(row[2],str(file_name)))
                qr.make(fit=True)

                qr_image = qr.make_image(fill_color="black", back_color="white")
                qr_position = (550, 20)
                image.paste(qr_image, qr_position)
                
                #qr end
                
                custom_font_path = "oykobold.ttf"
                text = 'Participant : {} \nEmail : {}\nCollege : {} \nMobile : {}\nEvent : {} \nAmount Paid : {}'.format(row[1], row[2], truncate_string(row[4], 32),row[3],file_name, "yes")
                text_color = "white"
                custom_font = ImageFont.truetype(custom_font_path, 22)
                draw.text((20, 90), text, font=custom_font, fill=text_color)
                
                filename = './'+file_name+'/{}.png'.format(row[1])
                image.save(filename)
                subject = "Confirmation regarding online registeration in Adhyaaya'24"
                body = "Dear Participant,\n"+"We are excited to inform you that your registration for the Adhyaaya Technical fest has been confirmed. \nWe are sending you an attachment of your reciept so that we can authenticate you in the event.\n Join us for a fantastic event filled with technical challenges, workshops, and networking opportunities. Have fun! \nBest regards,\nAdhyaaya Technical Team"
                to_email = "tanishqbakka1@gmail.com"
                image_path = filename 
                send_email(subject, body, to_email, image_path, smtp_server, smtp_port, smtp_username, smtp_password)


                


