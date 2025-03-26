import heapq

# Definição do mapa da Romênia como um grafo com pesos
romenia_mapa = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Heurística: distância em linha reta até Bucharest
heuristica = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Timisoara': 329, 'Lugoj': 244,
    'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160, 'Sibiu': 253, 'Fagaras': 176,
    'Rimnicu Vilcea': 193, 'Pitesti': 100, 'Bucharest': 0, 'Giurgiu': 77,
    'Urziceni': 80, 'Hirsova': 151, 'Eforie': 161, 'Vaslui': 199, 'Iasi': 226,
    'Neamt': 234
}

def busca_a_estrela(inicio, destino):
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0 + heuristica[inicio], 0, inicio))
    visitados = set()
    caminho = {}
    custos = {inicio: 0}
    
    while fila_prioridade:
        _, custo_atual, cidade_atual = heapq.heappop(fila_prioridade)
        
        if cidade_atual == destino:
            return reconstruir_caminho(caminho, inicio, destino)
        
        visitados.add(cidade_atual)
        
        for vizinho, custo in romenia_mapa[cidade_atual].items():
            novo_custo = custo_atual + custo
            
            if vizinho not in visitados or novo_custo < custos.get(vizinho, float('inf')):
                custos[vizinho] = novo_custo
                prioridade = novo_custo + heuristica[vizinho]
                heapq.heappush(fila_prioridade, (prioridade, novo_custo, vizinho))
                caminho[vizinho] = cidade_atual
    
    return None  # Nenhum caminho encontrado

# Reconstrução do caminho percorrido
def reconstruir_caminho(caminho, inicio, destino):
    percurso = []
    atual = destino
    while atual != inicio:
        percurso.append(atual)
        atual = caminho[atual]
    percurso.append(inicio)
    return list(reversed(percurso))

# Executando a busca A* de Arad para Bucharest
resultado = busca_a_estrela('Arad', 'Bucharest')
print("Caminho encontrado:", resultado)
