from threading import Lock

class Projector:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.lock = Lock()
        self.is_available = True

    def reserve(self):
        with self.lock:
            if self.is_available:
                self.is_available = False
                return True
            return False

    def release(self):
        with self.lock:
            self.is_available = True