import csv
import os
import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import random


width, height = 640, 240
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

bg_array = []
for i in range(0,25):
    bg_array.append("bg_{}.jpg".format(i))
    
random.shuffle(bg_array)

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
                
                
                
                #eventDetails
                custom_font_path = "oykobold.ttf"
                text = 'Event Details \nDate : 20/02/2024 \nTime : 11:30 PM'
                text_color = "white"
                custom_font = ImageFont.truetype(custom_font_path, 13)
                draw.text((405, 30), text, font=custom_font, fill=text_color)
                
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
                


