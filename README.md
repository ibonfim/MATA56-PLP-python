# MATA56-PLP-python

## Sistema de Reserva de Datashows

Este projeto implementa um sistema de reserva de datashows usando threads para simular múltiplos usuários tentando acessar os recursos simultaneamente. O código usa mecanismos de sincronização para garantir que as reservas sejam feitas de forma segura.

### Funcionalidades

- **Reserva de datashows** de forma concorrente.
- **Controle de acesso** via `threading.Lock` para evitar condições de corrida.
- **Simulação de múltiplos usuários** tentando reservar os recursos.

### Estrutura do Código

#### Classe `SistemaDeReserva`

A classe é responsável por gerenciar a reserva e liberação dos datashows.

- `__init__(num_datashows)`: Inicializa a quantidade de datashows disponíveis.
- `reservar_datashow(usuario_id)`: Tenta reservar um datashow disponível. Se todos estiverem ocupados, o usuário não consegue reservar.

#### Função `simular_reservas`

Função que recebe uma instância do sistema e um identificador de usuário para simular uma tentativa de reserva.

### Fluxo de execução

1. Inicializa o sistema com 3 datashows.
2. Cria 10 threads para simular 10 usuários tentando fazer reservas.
3. Cada thread tenta reservar um datashow e libera após um tempo simulado de uso.
