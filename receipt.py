from PIL import Image, ImageDraw, ImageFont

width, height = 640, 240
image = Image.new("RGBA", (width, height), (255, 255, 255, 0))



image_to_add_path = "bg.png"
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

custom_font_path = "./font-2.ttf"

text = "Participant Details "
text_color = "gold"


custom_font = ImageFont.truetype(custom_font_path, 48)
draw.text((20, 20), text, font=custom_font, fill=text_color)

custom_font_path = "./font-4.ttf"

text =' Participant Name : Tanishq Dhote \n Event Name : Roborace \n Amount Paid : Yes'
text_color = "white"

custom_font = ImageFont.truetype(custom_font_path, 24)
draw.text((20, 100), text, font=custom_font, fill=text_color)

image.save("output_image.png")

image.show()
