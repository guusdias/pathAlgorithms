import heapq

# Definindo o estado inicial e final
initial_state = ('sala1', 1, 1, 1)
goal_state = ('sala1', 0, 0, 0)

# Definindo a heurística (número de salas ainda sujas)
def heuristic(state):
    _, y, z, w = state
    return y + z + w

# Função que gera os sucessores (próximos estados possíveis)
def successors(state):
    room, y, z, w = state
    succ = []

    if room == 'sala1':
        if y == 1:
            succ.append(('sala1', 0, z, w))
        succ.append(('sala2', y, z, w))
        succ.append(('sala3', y, z, w))
    elif room == 'sala2':
        if z == 1:
            succ.append(('sala2', y, 0, w))
        succ.append(('sala1', y, z, w))
        succ.append(('sala3', y, z, w))
    elif room == 'sala3':
        if w == 1:
            succ.append(('sala3', y, z, 0))
        succ.append(('sala1', y, z, w))
        succ.append(('sala2', y, z, w))
    
    return succ

# Função que implementa o algoritmo A*
def a_star(initial_state, goal_state):
    queue = []
    heapq.heappush(queue, (heuristic(initial_state), initial_state))
    visited = set()
    came_from = {initial_state: None}
    cost_so_far = {initial_state: 0}

    while queue:
        _, current = heapq.heappop(queue)
        
        if current == goal_state:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        if current in visited:
            continue
        
        visited.add(current)

        for successor in successors(current):
            new_cost = cost_so_far[current] + 1  # Custo para cada movimento
            if successor not in cost_so_far or new_cost < cost_so_far[successor]:
                cost_so_far[successor] = new_cost
                priority = new_cost + heuristic(successor)
                heapq.heappush(queue, (priority, successor))
                came_from[successor] = current
    
    return None

# Executando o algoritmo A*
path = a_star(initial_state, goal_state)
print("Caminho encontrado:")
for step in path:
    print(step)
