import threading
import time
import random

class SistemaReserva:
    def __init__(self):
        # Salas e seus datashows disponíveis
        self.salas = {"Sala1": None, "Sala2": None, "Sala3": None}
        self.datashows_disponiveis = ["Datashow1", "Datashow2", "Datashow3"]
        self.lock = threading.Lock()

    def reservar_datashow(self, sala):
        """Tenta reservar um datashow para uma sala."""
        with self.lock:
            # Verifica se a sala já tem um datashow alocado
            if self.salas[sala] is not None:
                print(f"[{threading.current_thread().name}] A {sala} já tem {self.salas[sala]} reservado.")
                return

            # Verifica se há datashows disponíveis
            if not self.datashows_disponiveis:
                print(f"[{threading.current_thread().name}] Não há datashows disponíveis para {sala}.")
                return

            # Reserva o primeiro datashow disponível
            datashow = self.datashows_disponiveis.pop(0)
            self.salas[sala] = datashow
            print(f"[{threading.current_thread().name}] {datashow} foi reservado para {sala}.")

    def liberar_datashow(self, sala):
        """Libera o datashow de uma sala."""
        with self.lock:
            if self.salas[sala] is None:
                print(f"[{threading.current_thread().name}] Não há datashow para liberar em {sala}.")
                return

            # Libera o datashow e o adiciona à lista de disponíveis
            datashow = self.salas[sala]
            self.salas[sala] = None
            self.datashows_disponiveis.append(datashow)
            print(f"[{threading.current_thread().name}] {datashow} foi liberado de {sala}.")

def solicitar_reserva(sistema, sala):
    """Função para simular uma solicitação de reserva."""
    sistema.reservar_datashow(sala)
    time.sleep(random.uniform(0.5, 2))
    sistema.liberar_datashow(sala)

if __name__ == "__main__":
    # Criação do sistema de reservas
    sistema = SistemaReserva()

    # Lista de threads para simular solicitações simultâneas
    threads = []
    for i in range(5):  # Simular 5 solicitações
        sala = random.choice(["Sala1", "Sala2", "Sala3"])
        thread = threading.Thread(target=solicitar_reserva, args=(sistema, sala), name=f"Thread-{i+1}")
        threads.append(thread)

    # Iniciar as threads
    for thread in threads:
        thread.start()

    # Aguardar todas as threads terminarem
    for thread in threads:
        thread.join()

    print("\nEstado final do sistema:")
    print("Salas:", sistema.salas)
    print("Datashows disponíveis:", sistema.datashows_disponiveis)
