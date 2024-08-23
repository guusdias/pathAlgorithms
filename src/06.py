'''
6. Implemente um algoritmo de busca A* para problema de deslocamento pelo mapa da
Romênia. O objetivo do problema é ir de Arad até Bucharest no menor caminho possível.
Além disso, o algoritmo deve visitar o menor número possível de estados candidatos.
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

def a_star_search(start, goal):
    if start not in graph or goal not in graph:
        return []

    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while open_list:
        _, current_cost, current = heapq.heappop(open_list)

        if current == goal:
            break

        for neighbor, cost in graph.get(current, {}).items():
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristics[neighbor]
                heapq.heappush(open_list, (priority, new_cost, neighbor))
                came_from[neighbor] = current
    path = []
    step = goal
    while step is not None:
        path.append(step)
        step = came_from.get(step)
    path.reverse()

    if path[0] == start:
        return path
    else:
        return []

start_city = 'Arad'
goal_city = 'Bucharest'
path = a_star_search(start_city, goal_city)
print(f'Caminho encontrado: {" -> ".join(path) if path else "Nenhum caminho encontrado"}')

'''
O código implementa o algoritmo A* para encontrar o caminho mais curto de Arad até Bucharest em um mapa da Romênia, considerando tanto o custo real de deslocamento entre as cidades quanto uma heurística que estima a distância restante até o destino. O grafo representa as cidades e as distâncias entre elas, enquanto as heurísticas fornecem uma estimativa da proximidade de cada cidade a Bucharest. O algoritmo explora os estados (cidades) com base no menor custo total (custo do caminho percorrido mais a estimativa de distância restante), garantindo assim a busca pelo caminho mais eficiente. Ao alcançar Bucharest, o caminho percorrido é reconstruído e impresso. Se nenhum caminho é encontrado, uma mensagem indicativa é exibida.
'''