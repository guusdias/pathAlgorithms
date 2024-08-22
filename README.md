# Tarefa de Inteligência Artificial: Resolução de Problemas

## Descrição

Esta tarefa tem como objetivo implementar e testar algoritmos clássicos de busca de caminhos e resolução de problemas. Os algoritmos abordados incluem:

- **Busca em Largura (BFS)**
- **Busca em Profundidade (DFS)**
- **Busca A\***
- **Algoritmo de Dijkstra**

Os problemas a serem resolvidos incluem a navegação em labirintos, o jogo das oito peças (8-puzzle) e outros problemas de otimização e planejamento.

## Estrutura do Projeto

- `src/`: Diretório contendo os arquivos de código fonte.
  - `bfs.py`: Implementação do algoritmo de Busca em Largura.
  - `dfs.py`: Implementação do algoritmo de Busca em Profundidade.
  - `a_star.py`: Implementação do algoritmo A*.
  - `dijkstra.py`: Implementação do algoritmo de Dijkstra.
  - `maze_solver.py`: Script para resolver labirintos utilizando os algoritmos implementados.
  - `eight_puzzle.py`: Script para resolver o jogo das oito peças utilizando os algoritmos implementados.

- `tests/`: Diretório contendo scripts de testes e exemplos de entrada.

- `README.md`: Este arquivo.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas necessárias: (listadas no `requirements.txt`)

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd nome-do-repositorio
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute os scripts para testar os algoritmos:
   ```bash
   python src/maze_solver.py
   ```

5. Para executar os testes, utilize:
   ```bash
   python -m unittest discover tests
   ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork do projeto e enviar pull requests.
