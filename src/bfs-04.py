'''
4. Crie uma representação do espaço de estados para o problema do quebra-cabeça de 8
peças. O problema consiste em mover peças do quebra-cabeça na horizontal ou
vertical, de modo que a configuração final seja alcançada. Os movimentos realizados
devem fazer com que a peça em questão ocupe a posição vazia adjacente à ela. Os
movimentos devem ser sequencialmente realizados modo que a configuração final
seja alcançada. Após criar a representação do espaço de estados, crie um algoritmo
de busca para solucionar o problema.
'''


def dfs(estado_inicial):
    pilha = [estado_inicial]
    visitados = set()
    visitados.add(str(estado_inicial))

    while pilha:
        estado_atual = pilha.pop()

        if estado_atual == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return estado_atual

        novos_estados = gerar_novos_estados(estado_atual)

        for novo_estado in novos_estados:
            estado_str = str(novo_estado)
            if estado_str not in visitados:
                pilha.append(novo_estado)
                visitados.add(estado_str)

    return None


def encontrar_vazio(estado):
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                return i, j


def gerar_novos_estados(estado):
    i, j = encontrar_vazio(estado)
    novos_estados = []

    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for movimento in movimentos:
        novo_i, novo_j = i + movimento[0], j + movimento[1]

        if 0 <= novo_i < 3 and 0 <= novo_j < 3:
            novo_estado = [linha[:] for linha in estado]

            novo_estado[i][j], novo_estado[novo_i][novo_j] = \
                novo_estado[novo_i][novo_j], novo_estado[i][j]

            novos_estados.append(novo_estado)

    return novos_estados


estado_inicial = [[4, 2, 7], [8, 0, 6], [3, 5, 1]]

solucao = dfs(estado_inicial)

if solucao:
    print("Quebra-cabeça resolvido:")
    for linha in solucao:
        print(linha)
else:
    print("Nenhuma solução encontrada.")
