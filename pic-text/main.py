from PIL import Image, ImageDraw, ImageFont

img_text_size = 15
text = "月是故乡明"
text_path = './Alibaba-PuHuiTi-Bold.ttf'
font = ImageFont.truetype(text_path, img_text_size)
img_path = './deng.png'

img = Image.open(img_path)
img_w, img_h = img.size

c_img = Image.new("RGB", (img_text_size, img_text_size))
n_img = Image.new("RGB", (img_text_size * img_w, img_text_size * img_h))

text_w, text_h = font.getsize("中")  # 获取单个文字的宽、高
offset_x = (img_text_size - text_w) >> 1  # 文字水平居中
offset_y = (img_text_size - text_h) >> 1  # 文字垂直居中

char_index = 0
draw = ImageDraw.Draw(c_img)  # 小图的绘图对象，用于绘制文字

for x in range(img_w):  # 宽在外 高在内，因此文字的方向是从左到右，从上到下排列的
    for y in range(img_h):
        draw.rectangle((0, 0, img_text_size, img_text_size), fill='lightgray')  # 绘制背景，看起来会好一些
        draw.text((offset_x, offset_y), text[char_index], font=font, fill=img.getpixel((x, y)))  # 用（x,y）处像素点的色值绘制字体
        n_img.paste(c_img, (x * img_text_size, y * img_text_size))
        char_index = (char_index + 1) % len(text)

n_img.save('moon-text4.png')
