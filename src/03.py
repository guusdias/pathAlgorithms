'''
O código apresentado implementa uma solução para o problema do fazendeiro, onde o objetivo é atravessar um rio com três itens (uma galinha, uma raposa e um milho), respeitando certas restrições de segurança. O fazendeiro deve garantir que, sem sua presença, nenhum dos itens seja consumido por outro item. O algoritmo adota uma abordagem de busca para encontrar uma sequência de estados que leva ao objetivo final.

A classe FarmerProblem herda da classe Problem e define três entidades a serem transportadas: 'chicken', 'fox', e 'corn'. No início, o fazendeiro e todas as entidades estão na margem esquerda do rio. O método is_safe avalia se a configuração atual dos itens é segura, evitando combinações perigosas. A função is_goal_reached verifica se todos os itens e o fazendeiro chegaram à margem direita.

Para explorar todos os estados possíveis, o método expand_states cria novos estados com base nas ações possíveis: o fazendeiro pode se mover sozinho ou com uma das entidades. Apenas os estados seguros são adicionados à lista de estados filhos. O método find_solution utiliza uma abordagem de busca para encontrar a sequência de estados que leva ao objetivo. Ele adiciona novos estados à lista path até encontrar a solução.

Os métodos auxiliares state_of, move, e check_and_add_child ajudam a manipular e verificar o estado das entidades e garantir que apenas estados válidos sejam explorados. A função format_output é responsável por formatar e exibir o caminho encontrado de forma legível, listando a configuração de itens em cada margem do rio ao longo da solução.
'''
class Problem:
    def __init__(self, initial_state, goal_state=None):
        self.initial_state = initial_state
        self.goal_state = goal_state


class FarmerProblem(Problem):
    entities = ['chicken', 'fox', 'corn']

    def __init__(self, initial_state, goal_state=None):
        super().__init__(initial_state, goal_state)

    @staticmethod
    def is_safe(state):
        if state_of('farmer', state) == state_of('chicken', state):
            return True
        elif state_of('chicken', state) == state_of('fox', state):
            return False
        elif state_of('chicken', state) == state_of('corn', state):
            return False
        else:
            return True

    @staticmethod
    def is_goal_reached(state):
        return all(state_of(e, state) == 'right' for e in ['farmer'] + FarmerProblem.entities)

    @staticmethod
    def expand_states(state):
        children = []
        child = state.copy()
        move('farmer', child)
        check_and_add_child(child, children)
        for ent in FarmerProblem.entities:
            if state_of(ent, state) == state_of('farmer', state):
                child = state.copy()
                move('farmer', child)
                move(ent, child)
                check_and_add_child(child, children)
        return children

    def find_solution(self):
        path = [self.initial_state]
        next_state = self.initial_state.copy()
        while next_state and not self.is_goal_reached(next_state):
            new_states = self.expand_states(next_state)
            next_state = {}
            for child in new_states:
                if not (child in path):
                    next_state = child
                    path.append(next_state)
                    break
        return path


def state_of(who, state):
    try:
        return state[who]
    except KeyError:
        state[who] = 'left'
        return 'left'


def move(who, state):
    if state[who] == 'left':
        state[who] = 'right'
    else:
        state[who] = 'left'
    return state


def check_and_add_child(child, state_list):
    if FarmerProblem.is_safe(child):
        state_list.append(child)
    return state_list


initial_state = {'farmer': 'left'}
for e in FarmerProblem.entities:
    initial_state[e] = 'left'

problem = FarmerProblem(initial_state)
solution_path = problem.find_solution()
formatted_results = []

def format_output(state, prev_state=None):
    ENTITY_NAMES = {
        'farmer': 'Farmer',
        'chicken': 'Chicken',
        'fox': 'Fox',
        'corn': 'Corn'
    }

    left = [ENTITY_NAMES.get(k, k.capitalize()) for k, v in state.items() if v == 'left']
    right = [ENTITY_NAMES.get(k, k.capitalize()) for k, v in state.items() if v == 'right']

    formatted_output = (
        f"{len(formatted_results) + 1} - Left [{', '.join(left)}] - River - [{', '.join(right)}] Right\n\n"
    )
    formatted_results.append(formatted_output)
    return formatted_output

print("The path is: \n")
for state in solution_path:
    previous_state = state
    print(format_output(state, prev_state=previous_state))
