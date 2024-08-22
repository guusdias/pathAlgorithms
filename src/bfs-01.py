'''
1. Implemente um algoritmo de busca para o problema do mundo do aspirador, mas neste caso, prevendo três salas a serem aspiradas. Utilize uma estratégia que evite ciclos durante o processo de busca.

- Exemplo de representação dos estados tupla \[X, Y, Z, W\]
  - X ∈ {sala1, sala2, sala3}: indica a localização do aspirador
  - Y ∈ {0,1}: indica a situação da sala1 (0 está limpa e 1 está suja)
  - Z ∈ {0,1}: indica a situação da sala2 (0 está limpa e 1 está suja)
  - W ∈ {0,1}: indica a situação da sala3 (0 está limpa e 1 está suja)
  
- Exemplo de representação das ações
  - oper(aspirar, \[sala1,Y,Z,W\], \[sala1,0,Z,W\]) ← Y = 1
  - oper(aspirar, \[sala2,Y,Z,W\], \[sala2,Y,0,W\]) ← Z = 1
  - oper(aspirar, \[sala3,Y,Z,W\], \[sala3,Y,Z,0\]) ← W = 1
  - oper(entrarSala1, \[X,Y,Z,W\], \[sala1,Y,Z,W\]) ← X = sala2
  - oper(entrarSala1, \[X,Y,Z,W\], \[sala1,Y,Z,W\]) ← X = sala3
  - oper(entrarSala2, \[X,Y,Z,W\], \[sala2,Y,Z,W\]) ← X = sala1
  - oper(entrarSala2, \[X,Y,Z,W\], \[sala2,Y,Z,W\]) ← X = sala3
  - oper(entrarSala3, \[X,Y,Z,W\], \[sala3,Y,Z,W\]) ← X = sala1
  - oper(entrarSala3, \[X,Y,Z,W\], \[sala3,Y,Z,W\]) ← X = sala2
'''

from collections import deque

# Estado representado como uma tupla (X, Y, Z, W)
# X indica a localização do aspirador (sala1, sala2, sala3)
# Y indica se a sala1 está limpa (0) ou suja (1)
# Z indica se a sala2 está limpa (0) ou suja (1)
# W indica se a sala3 está limpa (0) ou suja (1)

def aspirar_estado(estado):
    X, Y, Z, W = estado
    if X == 'sala1' and Y == 1:
        return (X, 0, Z, W)
    elif X == 'sala2' and Z == 1:
        return (X, Y, 0, W)
    elif X == 'sala3' and W == 1:
        return (X, Y, Z, 0)
    return estado  

def mover_para_sala(estado, nova_sala):
    X, Y, Z, W = estado
    return (nova_sala, Y, Z, W)

def busca_solucao(estado_inicial):
    visitados = set()  
    fila = deque([(estado_inicial, [])]) 

    while fila:
        estado_atual, caminho = fila.popleft()

        if estado_atual in visitados:
            continue

        visitados.add(estado_atual)

        X, Y, Z, W = estado_atual
        if Y == 0 and Z == 0 and W == 0:
            return caminho  

        novas_acoes = []

        novo_estado = aspirar_estado(estado_atual)
        if novo_estado != estado_atual:
            novas_acoes.append(('aspirar', novo_estado))

        for sala in ['sala1', 'sala2', 'sala3']:
            if sala != X: 
                novo_estado = mover_para_sala(estado_atual, sala)
                novas_acoes.append((f'mover para {sala}', novo_estado))

        for acao, novo_estado in novas_acoes:
            novo_caminho = caminho + [acao]
            fila.append((novo_estado, novo_caminho))

    return None  

estado_inicial = ('sala1', 1, 1, 1)  

solucao = busca_solucao(estado_inicial)

if solucao:
    print("Solução encontrada:")
    for acao in solucao:
        print(acao)
else:
    print("Nenhuma solução encontrada.")
