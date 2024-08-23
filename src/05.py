'''
5. Implemente um algoritmo de busca gulosa para problema de deslocamento pelo mapa
da Romênia. O objetivo do problema é ir de Arad até Bucharest no menor caminho
possível. Além disso, o algoritmo deve visitar o menor número possível de estados
candidatos.
'''

import heapq

graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucharest': 101},
    'Craiova': {'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Bucharest': {}
}

heuristics = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Fagaras': 178,
    'Rimnicu Vilcea': 193,
    'Pitesti': 98,
    'Craiova': 160,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Bucharest': 0
}

def greedy_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], start))
    came_from = {}
    came_from[start] = None

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            break

        for neighbor, cost in graph.get(current, {}).items():
            if neighbor not in came_from:
                came_from[neighbor] = current
                heapq.heappush(open_list, (heuristics[neighbor], neighbor))
    path = []
    step = goal

    while step is not None:
        path.append(step)
        step = came_from.get(step)
    path.reverse()

    return path

start_city = 'Arad'
goal_city = 'Bucharest'
path = greedy_search(start_city, goal_city)
print(f'Caminho encontrado: {" -> ".join(path)}')


'''
O código implementa um algoritmo de busca gulosa para encontrar o caminho mais curto de Arad até Bucharest em um mapa da Romênia, utilizando heurísticas que estimam a distância restante até o destino. O grafo representa as cidades e as distâncias entre elas, enquanto as heurísticas fornecem uma estimativa da proximidade de cada cidade a Bucharest. O algoritmo prioriza a exploração dos estados (cidades) com a menor estimativa de distância (heurística) ao destino, visitando o menor número possível de estados candidatos. A busca continua até que Bucharest seja alcançada, e então o caminho é reconstruído e impresso.
'''