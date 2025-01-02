from time import gmtime
import guid


class Event:
    def __init__(self, trackId: int):
        self.trackId = trackId
        self.id = guid.new()
        self.timestamp = gmtime()

    def __str__(self):
        return f"{self.id.hex} {self.timestamp}"
