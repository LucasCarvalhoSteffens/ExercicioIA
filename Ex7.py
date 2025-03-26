import heapq
import math

def heuristic(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    directions = [
        (-1, 0, 10), (1, 0, 10), (0, -1, 10), (0, 1, 10),  # Laterais
        (-1, -1, 14), (-1, 1, 14), (1, -1, 14), (1, 1, 14)  # Diagonais
    ]
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for dx, dy, cost in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] != 'O':
                tentative_g_score = g_score[current] + cost
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # Sem caminho encontrado

# Definição do grid (substituir 'O' para obstáculos)
grid = [
    [70, 66, 62, 58, 54, 50],
    [66, 56, 52, 48, 42, 40],
    [62, 52, 42, 38, 'O', 30],
    [58, 48, 38, 'O', 20, 20],
    [54, 44, 34, 24, 14, 10],
    [50, 40, 30, 20, 10, 0]
]

start = (0, 0)  # Ponto de origem
goal = (5, 5)  # Ponto de destino

path = a_star_search(grid, start, goal)
print("Caminho encontrado:", path)