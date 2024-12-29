from PIL import Image

def quantize_image(image):
    img = image.convert('RGB')
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            r_quant = (r >> 5) << 5
            g_quant = (g >> 5) << 5
            b_quant = (b >> 6) << 6
            pixels[x, y] = (r_quant, g_quant, b_quant)
    return img

image = Image.open('finch.png')

width, height = image.size

quantized_image = quantize_image(image)
quantized_image = quantized_image.crop((200, 0, width - 200, height))
quantized_image = quantized_image.resize((128, 128))
image.show()
quantized_image.show()
