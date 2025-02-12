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

            try:
                opcao = int(input("Digite a opção desejada: "))
            except ValueError:
                print("Erro: Digite um número válido.")
                continue

            if opcao == 1:
                try:
                    projector_id = int(input("Digite o ID do projetor: "))
                    projector_name = input("Digite o nome do projetor: ")
                    service.add_projector(Projector(projector_id, projector_name))
                    print(f"Projetor '{projector_name}' adicionado com sucesso.")
                except ValueError:
                    print("Erro: O ID do projetor deve ser um número inteiro.")

            elif opcao == 2:
                try:
                    projector_id = int(input("Digite o ID do projetor que deseja reservar: "))
                    start_time = datetime.datetime.now()
                    end_time = start_time + datetime.timedelta(hours=2)
                    if service.reserve_projector(projector_id, start_time, end_time):
                        print(f"Projetor {projector_id} reservado com sucesso.")
                    else:
                        print(f"Falha ao reservar o projetor {projector_id}. ID inválido ou já está ocupado.")
                except ValueError:
                    print("Erro: O ID do projetor deve ser um número inteiro.")

            elif opcao == 3:
                start_time = datetime.datetime.now()
                end_time = start_time + datetime.timedelta(hours=2)
                try:
                    available_projectors = service.get_available_projectors(start_time, end_time)
                    if available_projectors:
                        print("Projetores disponíveis:")
                        for projector in available_projectors:
                            print(f"ID: {projector.id}, Nome: {projector.name}")
                    else:
                        print("Nenhum projetor disponível no momento.")
                except Exception as e:
                    print(f"Erro ao verificar projetores disponíveis: {e}")

            elif opcao == 4:
                try:
                    projector_id = int(input("Digite o ID do projetor que deseja liberar: "))
                    service.release_projector(projector_id)
                except ValueError:
                    print("Erro: O ID do projetor deve ser um número inteiro.")
                except Exception as e:
                    print(f"Erro ao liberar projetor: {e}")

            elif opcao == 5:
                try:
                    if not service.reservations:
                        print("Nenhum projetor reservado.")
                    else:
                        print("Projetores reservados:")
                        for projector in service.reservations:
                            print(f"ID: {projector.projector_id}, Início: {projector.start_time}, Fim: {projector.end_time}")
                except Exception as e:
                    print(f"Erro ao verificar projetores ocupados: {e}")

            elif opcao == 6:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    except KeyboardInterrupt:
        print("\nExecução interrompida pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()