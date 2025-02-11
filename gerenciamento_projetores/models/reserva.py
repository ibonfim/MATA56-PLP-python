from datetime import datetime

class Reservation:
    def __init__(self, projector_id: int, start_time: datetime, end_time: datetime):
        self.projector_id = projector_id
        self.start_time = start_time
        self.end_time = end_time

    def overlaps(self, other) -> bool:
        return self.start_time < other.end_time and self.end_time > other.start_time