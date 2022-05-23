import tkinter as tk
import PIL
from PIL import ImageTk, ImageDraw
import sys
import time

class RGBMatrix:
    def __init__(self, options):
        self.width = options.cols
        self.height = options.rows

        self._window = MatrixWindow()

    def SetImage(self, image, unsafe=True):
        if (image.mode != "RGB"):
            raise Exception("Currently, only RGB mode is supported for SetImage(). Please create images with mode 'RGB' or convert first with image = image.convert('RGB'). Pull requests to support more modes natively are also welcome :)")

        self._window.update_image(image)

class RGBMatrixOptions:
    def __init__(self):
        self.rows = None
        self.cols = None
        self.chain_length = None
        self.row_address_type = None
        self.multiplexing = None
        self.pwm_bits = None
        self.brightness = None
        self.pwm_lsb_nanoseconds = None
        self.led_rgb_sequence = None
        self.pixel_mapper_config = None
        self.show_refresh_rate = None
        self.gpio_slowdown = None
        self.disable_hardware_pulsing = None
        self.hardware_mapping = None

class MatrixWindow:
    WIDTH = 1024
    HEIGHT = WIDTH // 2

    def __init__(self):
        self._start_time = time.time()
        self._frames = 0

        self._root = tk.Tk()
        self._root.title("Virtual RGB Matrix")
        self._root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self._root.protocol("WM_DELETE_WINDOW", self.handle_close)

        self._canvas = tk.Canvas(self._root, width=self.WIDTH, height=self.HEIGHT)
        self._canvas.pack()

        self._current_image = None
        self._image_id = self._canvas.create_image(0, 0, anchor=tk.NW)
        self.update_window()

    def update_image(self, image):
        try:
            resized_image = image.resize((int(self._canvas["width"]), int(self._canvas["height"])), resample=PIL.Image.BOX)
            grid_image = self.draw_grid(resized_image)
            tk_image = ImageTk.PhotoImage(grid_image)
            self._current_image = tk_image
            self._canvas.itemconfig(self._image_id, image=self._current_image)
            self.update_window()
        except tk.TclError:
            pass

    def draw_grid(self, image):
        pixel_w = int(self._canvas["width"]) // 64
        pixel_h = int(self._canvas["height"]) // 32
        
        line_w_horizontal = pixel_w // 3
        line_w_vertical = pixel_h //3

        draw = ImageDraw.Draw(image)

        # Horizontal lines.
        for i in range(33):
            y = i * pixel_h
            draw.line([(0, y), (self.WIDTH, y)], fill="black", width=line_w_horizontal)

        # Vertical lines.
        for i in range(65):
            x = i * pixel_w
            draw.line([(x, 0), (x, self.HEIGHT)], fill="black", width=line_w_vertical)
        
        return image

    def update_window(self):
        try:
            self._root.title(f"Virtual RGB Matrix ({str(self.get_fps())} FPS)")
            self._root.update()
            self._root.update_idletasks()

            self._frames += 1
        except tk.TclError:
            sys.exit(0)

    def get_fps(self):
        return round(self._frames / (time.time() - self._start_time), 2)

    def handle_close(self):
        self._root.destroy()