'''
2. Implemente um algoritmo de busca para o problema dos jarros. O problema envolve por dois jarros com capacidades de 3 e 4 litros, respectivamente. Sabendo-se que podemos encher, esvaziar ou transferir água de um jarro para outro, encontre uma sequência de passos que deixe o jarro de 4 litros com exatamente 2 litros de água. Utilize uma estratégia que evite ciclos durante o processo de busca.
 
- Representação dos estados tupla [X, Y]
  - \( X \in \{0,1,2,3\} \): indica o conteúdo do jarro com capacidade de 3 litros
  - \( Y \in \{0,1,2,3,4\} \): indica o conteúdo do jarro com capacidade de 4 litros
 
- Representação das ações
  - \( \text{oper(enche1,[X,Y],[3,Y])} \leftarrow X < 3 \)
  - \( \text{oper(enche2,[X,Y],[X,4])} \leftarrow Y < 4 \)
  - \( \text{oper(esvazia1,[X,Y],[0,Y])} \leftarrow X > 0 \)
  - \( \text{oper(esvazia2,[X,Y],[X,0])} \leftarrow Y > 0 \)
  - \( \text{oper(transfere1para2,[X,Y],[0,X+Y])} \leftarrow X > 0, X+Y \leq 4 \)
  - \( \text{oper(transfere1para2,[X,Y],[X-(4-Y),4])} \leftarrow X > 0, Y < 4, X+Y > 4 \)
  - \( \text{oper(transfere2para1,[X,Y],[X+Y,0])} \leftarrow Y > 0, X+Y \leq 3 \)
  - \( \text{oper(transfere2para1,[X,Y],[3,Y-(3-X)])} \leftarrow X < 3, Y > 0, X+Y > 3 \)
'''

from collections import deque

def enche1(state):
    return [3, state[1]]

def enche2(state):
    return [state[0], 4]

def esvazia1(state):
    return [0, state[1]]

def esvazia2(state):
    return [state[0], 0]

def transfere1para2(state):
    X, Y = state
    transfer_amount = min(X, 4 - Y)
    return [X - transfer_amount, Y + transfer_amount]

def transfere2para1(state):
    X, Y = state
    transfer_amount = min(Y, 3 - X)
    return [X + transfer_amount, Y - transfer_amount]

def busca():
    estado_inicial = [0, 0]
    
    objetivo = 2
    
    fila = deque([(estado_inicial, [])])
    visitados = set()
    visitados.add(tuple(estado_inicial))
    
    while fila:
        estado_atual, caminho = fila.popleft() 
        
        if estado_atual[1] == objetivo:
            return caminho + [(estado_atual, "Objetivo alcançado!")]
        
        for operacao, funcao in [('encher-1', enche1), ('encher-2', enche2), 
                                 ('esvazia-1', esvazia1), ('esvazia-2', esvazia2), 
                                 ('transfere-1-para-2', transfere1para2), 
                                 ('transfere-2-para-1', transfere2para1)]:
            
            proximo_estado = funcao(estado_atual)
            if tuple(proximo_estado) not in visitados: 
                visitados.add(tuple(proximo_estado))
                fila.append((proximo_estado, caminho + [(estado_atual, operacao)]))
    
    return None

solucao = busca()
if solucao:
    print("Passos para alcançar a solução:")
    for passo, acao in solucao:
        print(f"Estado atual: Jarro X = {passo[0]}L, Jarro Y = {passo[1]}L -> Ação: {acao}")
else:
    print("Nenhuma solução encontrada.")


'''
O algoritmo implementado resolve o problema dos jarros utilizando uma técnica chamada busca em largura (BFS, do inglês Breadth-First Search). O problema envolve dois jarros, um com capacidade de 3 litros e outro com capacidade de 4 litros, e o objetivo é encontrar uma sequência de ações que deixe exatamente 2 litros no jarro maior (de 4 litros).
'''