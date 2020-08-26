from PIL import Image, ImageFilter

img = Image.open('.\\pokedesk\\pikachu.jpg')
filtered_image = img.filter(ImageFilter.SMOOTH)
filtered_image.save("blur.png",'png')
#print(img.format)