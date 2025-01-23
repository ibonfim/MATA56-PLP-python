Collecting workspace information

# Sistema de Reserva de Datashows

Este projeto implementa um sistema de reserva de datashows para salas utilizando threads para simular solicitações simultâneas.

## Funcionalidades

- **Reserva de Datashows**: Permite reservar um datashow disponível para uma sala específica.
- **Liberação de Datashows**: Permite liberar um datashow de uma sala, tornando-o disponível novamente.
- **Simulação de Solicitações Simultâneas**: Utiliza threads para simular múltiplas solicitações de reserva e liberação de datashows ao mesmo tempo.

## Estrutura do Código

- 

SistemaReserva

: Classe principal que gerencia as reservas e liberações de datashows.
  - 

reservar_datashow(sala)

: Tenta reservar um datashow para a sala especificada.
  - 

liberar_datashow(sala)

: Libera o datashow da sala especificada.
- 

solicitar_reserva(sistema, sala)

: Função que simula uma solicitação de reserva e liberação de datashow.
- Bloco 

if __name__ == "__main__":

: Cria o sistema de reservas e inicia múltiplas threads para simular solicitações simultâneas.

## Requisitos

- Python 3.x

## Como Rodar o Código

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Salve o código em um arquivo chamado 

atividade2_indaiara.py

.
3. Abra um terminal e navegue até o diretório onde o arquivo está salvo.
4. Execute o comando:

```sh
python atividade2_indaiara.py
```

## Fluxo de Execução

1. O sistema de reservas é criado instanciando a classe 

SistemaReserva

.
2. Uma lista de threads é criada para simular 5 solicitações simultâneas de reserva e liberação de datashows.
3. Cada thread escolhe aleatoriamente uma sala (`Sala1`, `Sala2` ou `Sala3`) e tenta reservar um datashow para essa sala.
4. Após reservar o datashow, a thread aguarda um tempo aleatório entre 0.5 e 2 segundos antes de liberar o datashow.
5. As threads são iniciadas e executadas simultaneamente.
6. O programa aguarda todas as threads terminarem antes de imprimir o estado final do sistema, mostrando quais salas têm datashows reservados e quais datashows estão disponíveis.

## Exemplo de Saída

```sh
[Thread-1] Datashow1 foi reservado para Sala2.
[Thread-2] Datashow2 foi reservado para Sala1.
[Thread-3] Datashow3 foi reservado para Sala3.
[Thread-4] Não há datashows disponíveis para Sala1.
[Thread-5] A Sala2 já tem Datashow1 reservado.
[Thread-1] Datashow1 foi liberado de Sala2.
[Thread-2] Datashow2 foi liberado de Sala1.
[Thread-3] Datashow3 foi liberado de Sala3.

Estado final do sistema:
Salas: {'Sala1': None, 'Sala2': None, 'Sala3': None}
Datashows disponíveis: ['Datashow1', 'Datashow2', 'Datashow3']
```

Este exemplo mostra como o sistema gerencia as reservas e liberações de datashows, garantindo que não haja conflitos ou reservas duplicadas.