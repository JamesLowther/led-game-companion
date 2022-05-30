import random
from time import sleep
from PIL import Image, ImageChops
from led_matrix.mario_kart.sources import CUPS
from led_matrix.common import msleep
from easing_functions import BackEaseOut
import numpy as np

class MarioKart:
    def __init__(self, matrix):
        self._matrix = matrix

        self._course_pool = set()
        self.generate_course_pool()

    def randomize(self):
        course_tape = self.generate_course_tape()
        self.transition(course_tape)

    def transition(self, course_tape):
        # sleep_amount = 4
        # SHIFT_AMOUNT = -2

        width = course_tape.size[0]

        sleep_easing = BackEaseOut(start=1, end=10, duration=width)
        shift_easing = BackEaseOut(start=3, end=2, duration=width)

        current_offset = 0

        while True:
            shift_amount = int(shift_easing.ease(current_offset) * -1)

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
            if current_offset > (width - self._matrix.dimensions[0]):
                break

            sleep_amount = sleep_easing.ease(current_offset)
            print(f"sleep {sleep_amount}")
            print(f"shift {shift_amount}\n")

            self._matrix.set_image(cropped)
            msleep(sleep_amount)

    def generate_course_tape(self, length=10):
        cup, course = self.pick_course()

        pre_courses = []

        # Generate course
        for _ in range(length-1):
            while True:
                cup_1 = random.choice(list(CUPS.keys()))
                course_1 = random.choice(list(CUPS[cup_1].keys()))

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
        return Image.open(CUPS[cup][course]["path"])

    def pick_course(self):
        if len(self._course_pool) == 0:
            self.generate_course_pool()
            print("empty")

        while True:
            cup = random.choice(list(CUPS.keys()))
            course = random.choice(list(CUPS[cup].keys()))

            if course in self._course_pool:
                self._course_pool.remove(course)
                return (cup, course)

    def generate_course_pool(self):
        for cup in CUPS.keys():
            for course in CUPS[cup].keys():
                self._course_pool.add(course)
