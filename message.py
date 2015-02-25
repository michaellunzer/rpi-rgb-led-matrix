import os
import datetime
import  pywapi
import string


from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

now = datetime.datetime.now()

yahoo_result = pywapi.get_weather_from_yahoo('97210', 'imperial')

print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "F now in Portland.\n\n"

weather_condition = string.lower(yahoo_result['condition']['text']) 

weather_temp = yahoo_result['condition']['temp']


#text = (("h n d"), (255, 200, 100))

#text = (("Ra \n rry Pi ", (255, 0, 0)), ("and ", (0, 255, 0)), ("Adafruit", (0, 0, 255)))

#while 2>1:

text = (now.strftime("%I"), (0, 0, 255)), (now.strftime("%M"), (0, 255, 0)),  (now.strftime("%p"), (0, 0, 255))

#baseString = str(((now.strftime("%I"), (255, 255, 255)), (now.strftime("%M"), (0, 255, 0)), (now.strftime("%p"), (0, 0, 255))))

font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf", 12)
all_text = ""
for text_color_pair in text:
    t = text_color_pair[0]
    all_text = all_text + t
print(all_text)
width, ignore = font.getsize(all_text)
print(width)
im = Image.new("RGB", (width, 16), "black")
draw = ImageDraw.Draw(im)
x = 0;
for text_color_pair in text:
    t = text_color_pair[0]
    c = text_color_pair[1]
    print("t=" + t + " " + str(c) + " " + str(x))
    draw.text((x, 4), t, c, font=font)
    x = x + font.getsize(t)[0]

im.save("test.ppm")

im = Image.open("test.ppm")
draw = ImageDraw.Draw(im)
#draw.line((0, 0) + im.size, fill=128)
#draw.line((0, im.size[1], im.size[0], 0), fill=128)


#volume = os.system("mpc volume")

#if volume == "volume: 50%":
  #  draw.line((0,2) + (0 ,13), fill=128)

#else:
    #draw.line((0,5) + (0,10), fill=128)

if weather_condition == "sunny":
    draw.ellipse((28, 0) +(32, 4), fill="yellow")
    
elif weather_condition == "fair":
    draw.ellipse((28, 0) +(32, 4), fill="grey")
    draw.ellipse((23, 0) +(27, 4), fill="grey")
    draw.ellipse((18, 0) +(22, 4), fill="grey")
    
else:
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)


#draw.arc((28, 2) + (25, 4), fill="yellow") (


del draw

im.save("test.ppm")

os.system("./led-matrix -D 1 -r 16 test.ppm -m 0")

#time.sleep(5000) 