from datetime import datetime
from typing import List
from gerenciamento_projetores.models.projetor import Projector
from gerenciamento_projetores.models.reserva import Reservation

class ReservationService:
    def __init__(self):
        self.projectors = []
        self.reservations = []

    def add_projector(self, projector: Projector):
        self.projectors.append(projector)

    def reserve_projector(self, projector_id: int, start_time: datetime, end_time: datetime) -> bool:
        for reservation in self.reservations:
            if reservation.projector_id == projector_id and reservation.overlaps(Reservation(projector_id, start_time, end_time)):
                return False

        for projector in self.projectors:
            if projector.id == projector_id and projector.reserve():
                self.reservations.append(Reservation(projector_id, start_time, end_time))
                return True

        return False

    def release_projector(self, projector_id: int):
        projector_found = False
        for projector in self.projectors:
            if projector.id == projector_id:
                projector_found = True
                projector.release()
                self.reservations = [r for r in self.reservations if r.projector_id != projector_id or r.end_time <= datetime.now()]
                print(f"Projector {projector_id} liberado.")
                break
        if not projector_found:
            print(f"Projector {projector_id} não encontrado.")

    def get_available_projectors(self, start_time: datetime, end_time: datetime) -> List[Projector]:
        available_projectors = []
        for projector in self.projectors:
            is_available = True
            for reservation in self.reservations:
                if reservation.projector_id == projector.id and reservation.overlaps(Reservation(projector.id, start_time, end_time)):
                    is_available = False
                    break
            if is_available:
                available_projectors.append(projector)
        return available_projectors