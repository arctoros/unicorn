from PIL import Image, ImageOps

targetWidth = 128
targetHeight = 128
colourDepth = 5

original = Image.open("finch.png")
width, height = original.size
left = 200
top = 0
right = height + left
bottom = height

image = original.crop((left, top, right, bottom))
image = image.resize((targetHeight, targetWidth))
image = ImageOps.posterize(image, colourDepth)
image.show()
pixels = image.load()
file = open('image.dat', 'wb')

for x in range(targetWidth):
    for y in range(targetHeight):
        pixel = pixels[x, y]
        result = 0
        shift = [colourDepth * 2, colourDepth, 0]

        for i in range (3):
            colour = round(pixel[i] / (256 / pow(2, colourDepth)))
            result |= colour << shift[i]

        result = result.to_bytes(2, byteorder='little')
        file.write(result)
