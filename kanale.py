from PIL import Image

img = Image.open("priroda.jpg")

r, g, b = img.split() #rozdelil som obrazky na farebne kanaly

#vytvorime obrazky iba z kanalom ktory chceme, ostatne nastavime na prazdne
red_img = Image.merge("RGB", (r, Image.new("L", img.size), Image.new("L", img.size)))
green_img = Image.merge("RGB", (Image.new("L", img.size), g, Image.new("L", img.size)))
blue_img = Image.merge("RGB", (Image.new("L", img.size), Image.new("L", img.size), b))

red_img.show()
green_img.show()
blue_img.show()
#program ukaze 3 nove obrazky