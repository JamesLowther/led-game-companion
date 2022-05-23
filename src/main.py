from urllib.parse import uses_relative
import urllib3
import signal
import threading
import sys

from PIL import Image

from led_matrix.matrix import Matrix
from led_matrix.display_handler import DisplayHandler
from web.app import app

urllib3.disable_warnings()

class Main:
    def __init__(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

        # Create display handler.
        self._matrix = Matrix()
        self._display_handler = DisplayHandler(self._matrix)

        # Start flask in its own thread.
        self._flask_thread = threading.Thread(target=lambda: app.run(debug=True, use_reloader=False))
        self._flask_thread.daemon = True
        self._flask_thread.start()

        self._display_handler.start()

    def signal_handler(self, sig, frame):
        print("Main - Sending stop event...")

        self._display_handler.stop()

        print("Main - Stopped.")
        sys.exit(0)

if __name__ == "__main__":
    Main()
