import csv
import os
import qrcode
from PIL import Image, ImageDraw, ImageFont
import random
width, height = 640, 240
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

csv_file_path = './Virtual-Placement.csv'
eventName = 'virtual-placement'
folderName='./'+eventName
bg_array = []
for i in range(0,25):
    bg_array.append("bg_{}.jpg".format(i))

if not os.path.exists(folderName):
    os.makedirs(folderName)
def truncate_string(input_string, max_length):
    if len(input_string) > max_length:
        truncated_string = input_string[:max_length]
        return truncated_string+'...'
    else:
        return input_string
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        
        image_to_add_path = bg_array[random.randint(0,len(bg_array)-1)]
        #image_to_add_path='bg_17.jpg'
        image_to_add = Image.open(image_to_add_path)
        image_to_add = image_to_add.resize((640, 240))
        image_position = (0, 0)
        image.paste(image_to_add, image_position)
        
        image_to_add_path = "solid.png"
        image_to_add = Image.open(image_to_add_path).convert("RGBA")
        image_to_add = image_to_add.resize((150, 112))
        image_position = (420, 35)
        image.paste(image_to_add, image_position, image_to_add)
        
        draw = ImageDraw.Draw(image)
        custom_font_path = "font-2.ttf"
        text = "Participant Details "
        text_color = "gold"
        custom_font = ImageFont.truetype(custom_font_path, 48)
        draw.text((20, 20), text, font=custom_font, fill=text_color)
        
        # custom_font_path = "oykobold.ttf"
        # text = 'Event Details \nDate : 20/02/2024 \nTime : 11:30 PM'
        # text_color = "white"
        # custom_font = ImageFont.truetype(custom_font_path, 18)
        # draw.text((420, 35), text, font=custom_font, fill=text_color)
        
        #qr starts
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=2.2,
            border=4,
        )
        qr.add_data(f"http://example.com/authenticate?participant_id={row[0]}")
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_position = (460, 50)
        image.paste(qr_image, qr_position)
        
        #qr end
        
        custom_font_path = "oykobold.ttf"
        text = 'Participant : {} \nEmail : {}\nCollege : {} \nMobile : {}\nEvent : {} \nAmount Paid : {}'.format(row[1], row[2], truncate_string(row[4], 26),row[3],eventName, "yes")
        text_color = "white"
        custom_font = ImageFont.truetype(custom_font_path, 18)
        draw.text((20, 90), text, font=custom_font, fill=text_color)
        
        filename = folderName+'/{}.png'.format(row[1])
        image.save(filename.lower())
        


