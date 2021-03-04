from PIL import Image
img = Image.new("RGB",(300,200),"RGB(0,255,0)")

for x in range(0,100):
  for y in range (0,200):
    img.putpixel((x,y),(0,0,255))

for x in range(100,200):
  for y in range (0,200):
    img.putpixel((x,y),(255,255,255))

for x in range(200,300):
  for y in range (0,200):
    img.putpixel((x,y),(255,0,0))

img.save('FRANCE.jpg')
img.show()