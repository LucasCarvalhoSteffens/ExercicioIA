import heapq
from typing import List, Tuple, Optional

class EightPuzzleSolver:
    def __init__(self, initial_state: List[List[int]], goal_state: List[List[int]]):
        self.initial_state = initial_state
        self.goal_state = goal_state
    
    def flatten_state(self, state: List[List[int]]) -> Tuple[int, ...]:
        return tuple(num for row in state for num in row)
    
    def count_inversions(self, state: List[List[int]]) -> int:
        flat = [num for row in state for num in row if num != 0]
        inversions = sum(1 for i in range(len(flat)) for j in range(i + 1, len(flat)) if flat[i] > flat[j])
        return inversions
    
    def is_solvable(self, initial_state: List[List[int]]) -> bool:
        inversions = self.count_inversions(initial_state)
        return inversions % 2 == 0  # Correção para quebra-cabeça 3x3
    
    def find_blank(self, state: List[List[int]]) -> Tuple[int, int]:
        for i, row in enumerate(state):
            if 0 in row:
                return i, row.index(0)
        raise ValueError("Sem espaço em branco no estado")
    
    def get_neighbors(self, state: List[List[int]]) -> List[List[List[int]]]:
        neighbors = []
        blank_row, blank_col = self.find_blank(state)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for move_row, move_col in moves:
            new_row, new_col = blank_row + move_row, blank_col + move_col
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row.copy() for row in state]
                new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
                neighbors.append(new_state)
        
        return neighbors
    
    def manhattan_distance(self, state: List[List[int]]) -> int:
        pos = {num: (i, j) for i, row in enumerate(self.goal_state) for j, num in enumerate(row)}
        return sum(abs(i - pos[num][0]) + abs(j - pos[num][1]) for i, row in enumerate(state) for j, num in enumerate(row) if num != 0)
    
    def solve(self) -> Optional[List[List[List[int]]]]:
        if not self.is_solvable(self.initial_state):
            print("O quebra-cabeça NÃO É resolúvel!")
            return None
        
        heap = [(0, self.initial_state, [])]
        visited = set()
        
        while heap:
            _, current_state, path = heapq.heappop(heap)
            state_tuple = self.flatten_state(current_state)
            
            if state_tuple in visited:
                continue
            
            visited.add(state_tuple)
            
            if current_state == self.goal_state:
                return path + [current_state]
            
            for neighbor in self.get_neighbors(current_state):
                if self.flatten_state(neighbor) not in visited:
                    g = len(path)
                    h = self.manhattan_distance(neighbor)
                    heapq.heappush(heap, (g + h, neighbor, path + [current_state]))
        
        return None

def main():
    initial_state = [
        [4, 2, 7],
        [0, 8, 6],
        [3, 5, 1]
    ]
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    solver = EightPuzzleSolver(initial_state, goal_state)
    print("Número de inversões:", solver.count_inversions(initial_state))
    print("É resolúvel?", solver.is_solvable(initial_state))
    
    solution = solver.solve()
    
    if solution:
        print("Solução encontrada em", len(solution) - 1, "movimentos:")
        for i, state in enumerate(solution):
            print(f"\nPasso {i}:")
            for row in state:
                print(row)
    else:
        print("Nenhuma solução encontrada.")

if __name__ == "__main__":
    main()