import random
import os
from tkinter import Y

from PIL import Image, ImageChops, ImageFont, ImageDraw
from led_matrix.mario_kart.sources import CUPS
from led_matrix.common import msleep
from easing_functions import QuarticEaseIn
from config import Config

class MarioKart:
    def __init__(self, matrix):
        self._matrix = matrix

        self._course_pool = set()
        self.generate_course_pool()

    def randomize(self):
        course_tape = self.generate_course_tape()
        self.transition(course_tape)

    def transition(self, course_tape):

        width = course_tape.size[0] - self._matrix.dimensions[0]

        sleep_easing = QuarticEaseIn(start=1, end=50, duration=width)

        current_offset = 0

        while True:
            shift_amount = -2

            course_tape = ImageChops.offset(course_tape, shift_amount, 0)
            cropped = course_tape.crop(
                (
                    0,
                    0,
                    self._matrix.dimensions[0],
                    self._matrix.dimensions[1]
                )
            )

            current_offset += abs(shift_amount)
            if current_offset > width:
                break

            sleep_amount = sleep_easing.ease(current_offset)

            self._matrix.set_image(cropped)
            msleep(sleep_amount)

    def generate_course_tape(self, length=15):
        cup, course = self.pick_course()

        pre_courses = []

        # Generate course
        for _ in range(length-1):
            while True:
                cup_1 = random.choice(list(CUPS.keys()))
                course_1 = random.choice(list(CUPS[cup_1]["courses"].keys()))

                if not (cup_1, course_1) in pre_courses and course != course_1:
                    pre_courses.append((cup_1, course_1))
                    break

        image = Image.new("RGB", (self._matrix.dimensions[0] * length, self._matrix.dimensions[1]), color="black")

        for i, pre_course in enumerate(pre_courses):
            course_image = self.create_course_image(pre_course[0], pre_course[1])
            image.paste(course_image, (i * self._matrix.dimensions[0], 0))

        selected_course = self.create_course_image(cup, course)

        image.paste(selected_course, ((length - 1) * self._matrix.dimensions[0], 0))

        return image

    def create_course_image(self, cup, course):
        image = Image.open(CUPS[cup]["courses"][course]["path"])
        image = image.convert("RGBA")

        cup_image = Image.open(CUPS[cup]["path"])
        cup_image = cup_image.convert("RGBA")

        font_path = os.path.join(Config.FONTS, "resolution-3x4.ttf")
        f = ImageFont.truetype(font_path, 4)

        box_color = (0, 0, 0)
        box_opacity = int(0.7 * 255)
        text_color = (230, 230, 230)
        t_list = self.text_list(course, f)

        y_offset = self._matrix.dimensions[1] - (f.getsize(t_list[-1])[1] * len(t_list))

        overlay = overlay = Image.new('RGBA', self._matrix.dimensions, box_color+(0,))
        overlay_d = ImageDraw.Draw(overlay)

        overlay_d.rounded_rectangle(
            [
                self._matrix.dimensions[0] - f.getsize(t_list[-1])[0] - 1,
                0 + y_offset - 1,
                self._matrix.dimensions[0],
                f.getsize(t_list[-1])[1] * len(t_list) + y_offset
            ],
            radius=2,
            fill=box_color+(box_opacity,)
        )

        overlay_d.rounded_rectangle(
            [
                self._matrix.dimensions[0] - cup_image.size[0] - 3,
                1,
                self._matrix.dimensions[0] - 2,
                cup_image.size[1] + 2
            ],
            radius=2,
            fill=box_color+(box_opacity,)
        )

        image = Image.alpha_composite(image, overlay)
        d = ImageDraw.Draw(image)

        for i, text in enumerate(t_list):
            d.text(
                (
                    self._matrix.dimensions[0] - f.getsize(text)[0], 
                    i * f.getsize(text)[1] + y_offset - 1
                ),
                text,
                font=f,
                fill=text_color
            )

        image.paste(
            cup_image, 
            (
                self._matrix.dimensions[0] - cup_image.size[0] - 2, 
                2
            ),
            cup_image
        )

        return image

    def text_list(self, text, font):
        t_list = [text]

        while True:
            size = font.getsize(t_list[-1])

            if size[0] > self._matrix.dimensions[0]:
                split = t_list[-1].split(" ")
                
                t_list = t_list[:-1] + [split[0]] + [" ".join(split[1:])]

            else:
                return t_list


    def pick_course(self):
        if len(self._course_pool) == 0:
            self.generate_course_pool()
            print("empty")

        while True:
            cup = random.choice(list(CUPS.keys()))
            course = random.choice(list(CUPS[cup]["courses"].keys()))

            if course in self._course_pool:
                self._course_pool.remove(course)
                return (cup, course)

    def generate_course_pool(self):
        for cup in CUPS.keys():
            for course in CUPS[cup]["courses"].keys():
                self._course_pool.add(course)
