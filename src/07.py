'''
7.Implemente a busca A\* para o problema *path finding* utilizando distância Euclidiana.** O mapa deve ser representado por uma matriz \( M \times N \) e deve ser estabelecido o ponto de partida e o ponto de destino. Além disso, no caminho podem existir obstáculos que devem ser desviados. Para a heurística, considere as ações de movimentos laterais com o custo de 10 e as ações de movimentos na diagonal com custo de 14.
Legenda:
- Origem (representada em rosa)
- Destino (representado em verde)
- Obstáculo (representado em azul)
- Caminho (representado em laranja)

| 70 | 66 | 62 | 58 | 54 | 50 |
|----|----|----|----|----|----|
| 66 | 56 | 52 | 48 | 44 | 40 |
|----|----|----|----|----|----|
| 62 | 52 | 42 | 38 | 34 | 30 |
|----|----|----|----|----|----|
| 58 | 48 | 38 | 28 | 24 | 20 |
|----|----|----|----|----|----|
| 54 | 44 | 34 | 24 | 14 | 10 |
|----|----|----|----|----|----|
| 50 | 40 | 30 | 20 | 10 |  0 |


O diagrama ao lado da matriz ilustra os possíveis movimentos, tanto laterais quanto diagonais.
'''
import heapq
import math

mapa = [
    [70, 66, 62, 58, 54, 50],
    [66, 56, 52, 48, 44, 40],
    [62, 52, 42, 38, 34, 30],
    [58, 48, 38, 28, 24, 20],
    [54, 44, 34, 24, 14, 10],
    [50, 40, 30, 20, 10, 0]
]

origem = (0, 0)  
destino = (5, 5)  

custo_lateral = 10

custo_diagonal = 14

def heuristica(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def a_estrela(mapa, origem, destino):
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, origem))

    custos = {origem: 0}
    came_from = {origem: None}

    while fila_prioridade:
        _, atual = heapq.heappop(fila_prioridade)

        if atual == destino:
            caminho = []
            while atual:
                caminho.append(atual)
                atual = came_from[atual]
            return caminho[::-1] 

        for dx, dy, custo in [(-1, 0, custo_lateral), (1, 0, custo_lateral), (0, -1, custo_lateral), (0, 1, custo_lateral),
                              (-1, -1, custo_diagonal), (-1, 1, custo_diagonal), (1, -1, custo_diagonal), (1, 1, custo_diagonal)]:
            vizinho = (atual[0] + dx, atual[1] + dy)

            if 0 <= vizinho[0] < len(mapa) and 0 <= vizinho[1] < len(mapa[0]):
                novo_custo = custos[atual] + custo
                
                if vizinho not in custos or novo_custo < custos[vizinho]:
                    custos[vizinho] = novo_custo
                    prioridade = novo_custo + heuristica(vizinho, destino)
                    heapq.heappush(fila_prioridade, (prioridade, vizinho))
                    came_from[vizinho] = atual

    return None  

caminho = a_estrela(mapa, origem, destino)

if caminho:
    print("Caminho encontrado:")
    for passo in caminho:
        print(passo)
else:
    print("Nenhum caminho encontrado.")


'''
O código implementa o algoritmo de busca A* para encontrar o caminho mais curto em um mapa representado por uma matriz, partindo de um ponto de origem até um ponto de destino. Ele utiliza a distância euclidiana como heurística para estimar a distância restante até o destino. O algoritmo explora os possíveis movimentos (laterais e diagonais) em torno de cada posição atual, priorizando aqueles com menor custo total estimado, que inclui o custo real do caminho percorrido e a estimativa da distância restante. Ao alcançar o destino, o código reconstrói o caminho percorrido e o imprime. Caso não encontre um caminho, informa que nenhum foi encontrado.'''