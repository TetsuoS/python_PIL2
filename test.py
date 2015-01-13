import Image

image = Image.open('1.png')
image = image.resize([512, 512])
image.save('2.png')
