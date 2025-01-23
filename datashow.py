import threading
import time

class SistemaDeReserva:
    def __init__(self, num_datashows):
        # Inicializa com a quantidade de datashows disponíveis
        self.datashows = [True] * num_datashows  # True significa disponível
        self.lock = threading.Lock()  # Lock para garantir que uma reserva seja feita de cada vez

    def reservar_datashow(self, usuario_id):
        # Tenta reservar um datashow
        with self.lock:  # Usando o lock para garantir que apenas uma thread acesse a função por vez
            for i in range(len(self.datashows)):
                if self.datashows[i]:  # Se o datashow estiver disponível
                    self.datashows[i] = False  # Marca o datashow como reservado
                    print(f"Usuário {usuario_id} reservou o datashow {i + 1}")
                    time.sleep(2)  # Simula o tempo de uso do datashow
                    self.datashows[i] = True  # Libera o datashow após o uso
                    print(f"Usuário {usuario_id} liberou o datashow {i + 1}")
                    return
            print(f"Usuário {usuario_id} não conseguiu reservar um datashow, todos estão ocupados.")

# Função que simula múltiplos usuários tentando fazer reservas
def simular_reservas(sistema, usuario_id):
    sistema.reservar_datashow(usuario_id)

# Cria o sistema com 3 datashows
sistema = SistemaDeReserva(3)

# Cria várias threads simulando usuários tentando reservar os datashows
threads = []
for i in range(10):  # Simula 10 usuários
    thread = threading.Thread(target=simular_reservas, args=(sistema, i+1))
    threads.append(thread)
    thread.start()

# Espera todas as threads terminarem
for thread in threads:
    thread.join()

print("Simulação finalizada.")
