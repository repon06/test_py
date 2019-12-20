from binascii import a2b_base64
from PIL import Image, ImageDraw
from io import BytesIO
from pathlib import Path
import os


def save_img_from_src(src, path):
    src_byte = a2b_base64(src)
    # fd = open('image.png', 'wb')
    # fd.write(binary_data)
    # fd.close()
    with open(path, 'wb') as f:
        f.write(src_byte)


def change_img(src, path):
    #    image = Image.open("C:/temp/image66.jpeg")

    with open(path, 'rb') as f:
        b = BytesIO()
        f.seek(15, 0)
        b.write(f.read())
        image = Image.open(b)
        image.load()

        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()

        factor = 10  # ввод int(input('factor:'))
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = a + b + c
                if (S > (((255 + factor) // 2) * 3)):
                    a, b, c = 255, 255, 255
                else:
                    a, b, c = 0, 0, 0
                draw.point((i, j), (a, b, c))

        file_name = os.path.splitext(os.path.basename(path))
        folder_path = os.path.dirname(path)
        image.save(f"{folder_path}/black/{file_name[0]}_blk{file_name[1]}", "JPEG")
        del draw
