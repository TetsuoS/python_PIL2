import Image

image = Image.open('1.png')
image = image.resize([256, 256])
image.save('2.png')
