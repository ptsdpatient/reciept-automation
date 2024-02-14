import csv
from PIL import Image, ImageDraw, ImageFont
import random
width, height = 640, 240
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))

csv_file_path = './respawn.csv'

bg_array = []
for i in range(0,25):
    bg_array.append("bg_{}.jpg".format(i))

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row if your CSV file has one
    next(csv_reader)
    
    for row in csv_reader:
        image_to_add_path = bg_array[random.randint(0,len(bg_array))]
        image_to_add = Image.open(image_to_add_path)
        image_to_add = image_to_add.resize((640, 240))
        image_position = (0, 0)
        image.paste(image_to_add, image_position)
        
        image_to_add_path = "solid.png"
        image_to_add = Image.open(image_to_add_path).convert("RGBA")
        image_to_add = image_to_add.resize((150, 112))
        image_position = (470, 110)
        image.paste(image_to_add, image_position, image_to_add)
        
        draw = ImageDraw.Draw(image)
        custom_font_path = "font-2.ttf"
        text = "Participant Details "
        text_color = "gold"
        custom_font = ImageFont.truetype(custom_font_path, 48)
        draw.text((20, 20), text, font=custom_font, fill=text_color)
        
        custom_font_path = "oykobold.ttf"
        text = 'Event Details \nDate : 20/02/2024 \nTime : 11:30 PM'
        text_color = "white"
        custom_font = ImageFont.truetype(custom_font_path, 18)
        draw.text((470, 35), text, font=custom_font, fill=text_color)
        
        
        custom_font_path = "oykobold.ttf"
        text = 'Participant Name : {} \nCollege : {} \nEvent : {} \nAmount Paid : {}'.format(row[1], row[2], row[3], "yes")
        text_color = "white"
        custom_font = ImageFont.truetype(custom_font_path, 24)
        draw.text((20, 90), text, font=custom_font, fill=text_color)
        
        filename = '{}.png'.format(row[1])
        image.save(filename.lower())
