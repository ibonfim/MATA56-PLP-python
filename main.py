from datetime import datetime, timedelta
from gerenciamento_projetores.models.projetor import Projector
from gerenciamento_projetores.services.reserva_service import ReservationService

import datetime

def main():
 
    service = ReservationService()
   # Adicionar projetores
    service.add_projector(Projector(1, "Projector 1"))
    service.add_projector(Projector(2, "Projector 2"))

    try:
        while True:
            print("1 - Adicionar projetor")
            print("2 - Reservar projetor")
            print("3 - Verificar projetores disponíveis")
            print("4 - Liberar projetor")
            print("5 - Verificar projetores ocupados")
            print("6 - Sair")

            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                projector_id = int(input("Digite o ID do projetor: "))
                projector_name = input("Digite o nome do projetor: ")
                service.add_projector(Projector(projector_id, projector_name))
            elif opcao == 2:
                projector_id = int(input("Digite o ID do projetor que deseja reservar: "))
                start_time = datetime.datetime.now()
                end_time = start_time + datetime.timedelta(hours=2)
                if service.reserve_projector(projector_id, start_time, end_time):
                    print(f"Projector {projector_id} reservado com sucesso.")
                else:
                    print(f"Falha ao reservar o Projector {projector_id}.Id invalido ou ele está ocupado.")
            elif opcao == 3:
                start_time = datetime.datetime.now()
                end_time = start_time + datetime.timedelta(hours=2)
                available_projectors = service.get_available_projectors(start_time, end_time)
                print("Projetores disponíveis:")
                for projector in available_projectors:
                    print(f"ID: {projector.id}, Nome: {projector.name}")
            elif opcao == 4:
                projector_id = int(input("Digite o ID do projetor que deseja liberar: "))
                service.release_projector(projector_id)
            elif opcao==5:
                if not service.reservations:
                    print("Nenhum projetor reservado.")
                for projector in service.reservations:
                    print(f"ID: {projector.projector_id}, Início: {projector.start_time}, Fim: {projector.end_time}")
                
            elif opcao == 6:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")

if __name__ == "__main__":
    main()