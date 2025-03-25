from collections import deque

def is_safe(state):
    """
    Verifica se o estado é seguro.
    
    :param state: Tupla representando o estado [Fazendeiro, Raposa, Galinha, Milho]
    :return: Boolean indicando se o estado é seguro
    """
    F, R, G, M = state
    
    # Regras de segurança:
    # 1. Se o fazendeiro não está presente, verificamos os outros elementos
    if F != R and R == G:  # Raposa e galinha sozinhas
        return False
    
    if F != G and G == M:  # Galinha e milho sozinhos
        return False
    
    return True

def get_possible_moves(state):
    """
    Gera todos os movimentos possíveis a partir do estado atual
    
    :param state: Estado atual
    :return: Lista de próximos estados possíveis
    """
    F, R, G, M = state
    possible_moves = []
    
    # Movimento do fazendeiro para o outro lado
    new_F = 'e' if F == 'd' else 'd'
    
    # Possíveis movimentos
    moves = [
        # Fazendeiro sozinho
        ((new_F, R, G, M), "vaiSozinho"),
        
        # Levando cada elemento
        ((new_F, new_F, G, M), "levaRaposa"),
        ((new_F, R, new_F, M), "levaGalinha"),
        ((new_F, R, G, new_F), "levaMilho")
    ]
    
    # Filtra apenas os movimentos seguros
    safe_moves = [
        (move, action) for move, action in moves if is_safe(move)
    ]
    
    return safe_moves

def solve_river_crossing():
    """
    Resolve o problema do fazendeiro atravessando o rio
    
    :return: Caminho da solução ou None
    """
    # Estado inicial: todos no lado esquerdo
    initial_state = ('e', 'e', 'e', 'e')
    
    # Estado objetivo: todos no lado direito
    goal_state = ('d', 'd', 'd', 'd')
    
    # Fila para busca em largura
    queue = deque([(initial_state, [])])
    
    # Conjunto para rastrear estados visitados
    visited = set()
    
    # Limite de iterações para evitar loop infinito
    max_iterations = 1000
    
    while queue:
        current_state, path = queue.popleft()
        
        # Pula estados já visitados
        if current_state in visited:
            continue
        
        visited.add(current_state)
        
        # Encontrou a solução
        if current_state == goal_state:
            return path
        
        # Explora próximos estados
        for next_state, action in get_possible_moves(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [action]))
    
    return None

def main():
    """
    Função principal para executar o solver
    """
    solution = solve_river_crossing()
    
    if solution:
        print("Solução encontrada:")
        for i, move in enumerate(solution, 1):
            print(f"Passo {i}: {move}")
    else:
        print("Nenhuma solução encontrada.")

if __name__ == "__main__":
    main()