import urllib3
import signal
import threading
import sys

from PIL import Image

from config import Config

from button_handler import ButtonHandler

from matrix import Matrix
from view_handler import ViewHandler

urllib3.disable_warnings()

class Main:
    def __init__(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

        Config.initialize_state()

        self._sigint_stop_event = threading.Event()
        self._press_event = threading.Event()
        self._long_press_event = threading.Event()

        self._button_thread = ButtonHandler(self._press_event, self._long_press_event, self._sigint_stop_event)
        
        if Config.VIRTUAL_MODE:
            self._button_thread.daemon = True
        self._button_thread.start()

        self._matrix = Matrix()

        self._view_handler = ViewHandler(self._matrix, self._press_event, self._long_press_event)
        self._view_handler.start()

    def signal_handler(self, sig, frame):
        print("Main - Sending stop event...")
        self._sigint_stop_event.set()

        self._view_handler.save_view()

        # Hack to clear screen on termination.
        image = Image.new("RGB", self._matrix.dimensions, color="black")     
        self._matrix.set_image(image)
        
        print("Main - Stopped.")
        sys.exit(0)

if __name__ == "__main__":
    Main()
