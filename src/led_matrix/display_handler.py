from queue import Queue, Empty
from PIL import Image
import uuid

from led_matrix.mario_kart.functions import MarioKart

class DisplayHandler:
    _command_queue = Queue()
    _finish_queue = Queue()
    _lock = False

    def __init__(self, matrix):
        self._matrix = matrix

        mario_kart = MarioKart(self._matrix)

        self._FUNCTION_MAPPINGS = {
            "mario-kart": {
                "randomize": mario_kart.randomize
            }
        }

    def start(self):
        while True:
            command_data = DisplayHandler._command_queue.get()
            DisplayHandler._lock = True

            command = command_data["command"]
            function = self._FUNCTION_MAPPINGS[command["game"]][command["function"]]

            # Compute.
            response = function()

            response_data = {
                "uuid": command_data["uuid"],
                "response": response
            }

            DisplayHandler._finish_queue.put(response_data)
            DisplayHandler._lock = False

    def stop(self):
        image = Image.new("RGB", self._matrix.dimensions, color="black")
        self._matrix.set_image(image)

    @classmethod
    def command(cls, command):
        c_id = uuid.uuid4()

        data = {
            "uuid": c_id,
            "command": command
        }

        if not cls._lock:
            cls._command_queue.put(data)
            return c_id

        return False

    @classmethod
    def wait_complete(cls):
        try:
            return cls._finish_queue.get(timeout=30)
        except Empty:
            cls._finish_queue.empty()
            return None
