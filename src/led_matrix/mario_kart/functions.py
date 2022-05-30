from PIL import Image
from led_matrix.mario_kart.sources import CUPS
import led_matrix.common

def randomize(matrix):

    for cup in CUPS.keys():
        for course in CUPS[cup].keys():
            print(f"{cup} : {course}")

            image = Image.open(CUPS[cup][course]["path"])
            matrix.set_image(image)

            led_matrix.common.msleep(1000)
