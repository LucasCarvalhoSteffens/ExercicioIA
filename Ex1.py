from collections import deque

class AspiradorTresSalas:
    def __init__(self, estado_inicial):
        self.estado_inicial = estado_inicial
        self.meta = (0, 0, 0)  # Todas as salas limpas

    def acoes_possiveis(self, estado):
        pos, y, z, w = estado
        acoes = []
        
        # Aspirar a sala atual
        if pos == "sala1" and y == 1:
            acoes.append(("aspirar", "sala1", 0, z, w))
        if pos == "sala2" and z == 1:
            acoes.append(("aspirar", "sala2", y, 0, w))
        if pos == "sala3" and w == 1:
            acoes.append(("aspirar", "sala3", y, z, 0))
        
        # Movimentação entre salas
        if pos == "sala1":
            acoes.append(("mover", "sala2", y, z, w))
        if pos == "sala2":
            acoes.append(("mover", "sala1", y, z, w))
            acoes.append(("mover", "sala3", y, z, w))
        if pos == "sala3":
            acoes.append(("mover", "sala2", y, z, w))
        
        return acoes

    def busca_largura(self):
        fila = deque([(self.estado_inicial, [])])
        visitados = set()
        
        while fila:
            (estado_atual, caminho) = fila.popleft()
            pos, y, z, w = estado_atual
            
            # Verifica se todas as salas estão limpas
            if (y, z, w) == self.meta:
                return caminho
            
            # Evita ciclos
            if estado_atual in visitados:
                continue
            visitados.add(estado_atual)
            
            # Expande os nós
            for acao, novo_pos, novo_y, novo_z, novo_w in self.acoes_possiveis(estado_atual):
                novo_estado = (novo_pos, novo_y, novo_z, novo_w)
                novo_caminho = caminho + [(acao, novo_estado)]
                fila.append((novo_estado, novo_caminho))
        
        return None  # Se não houver solução

# Estado inicial: aspirador na sala1 e todas as salas sujas
estado_inicial = ("sala1", 1, 1, 1)
aspirador = AspiradorTresSalas(estado_inicial)
caminho_solucao = aspirador.busca_largura()

print("Solução encontrada:")
for passo in caminho_solucao:
    print(passo)
