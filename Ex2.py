from collections import deque

def busca_jarros():
    capacidade1, capacidade2 = 3, 4  # Capacidades dos jarros
    estado_inicial = (0, 0)  # Ambos jarros vazios
    objetivo = 2  # Queremos 2 litros no jarro de 4 litros
    visitados = set()
    fila = deque([(estado_inicial, [])])
    
    while fila:
        (jarro1, jarro2), caminho = fila.popleft()
        
        if jarro2 == objetivo:
            return caminho + [(jarro1, jarro2)]  # Retorna o caminho percorrido
        
        if (jarro1, jarro2) in visitados:
            continue
        visitados.add((jarro1, jarro2))
        
        # Gerar novos estados
        acoes = [
            ((capacidade1, jarro2), "Encher jarro 1"),
            ((jarro1, capacidade2), "Encher jarro 2"),
            ((0, jarro2), "Esvaziar jarro 1"),
            ((jarro1, 0), "Esvaziar jarro 2"),
            ((max(0, jarro1 - (capacidade2 - jarro2)), min(capacidade2, jarro1 + jarro2)), "Transferir jarro 1 -> jarro 2"),
            ((min(capacidade1, jarro1 + jarro2), max(0, jarro2 - (capacidade1 - jarro1))), "Transferir jarro 2 -> jarro 1")
        ]
        
        for (novo_estado, acao) in acoes:
            if novo_estado not in visitados:
                fila.append((novo_estado, caminho + [(jarro1, jarro2, acao)]))
    
    return None  # Caso não encontre solução

solucao = busca_jarros()
if solucao:
    for estado in solucao:
        print(estado)
else:
    print("Nenhuma solução encontrada.")
