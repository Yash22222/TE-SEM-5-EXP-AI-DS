import heapq
import copy

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def calculate_heuristic(self):
        # Calculate the Manhattan distance heuristic
        heuristic = 0
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    x, y = divmod(self.state[i][j] - 1, 3)
                    heuristic += abs(i - x) + abs(j - y)
        return heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def a_star(initial_state):
    open_list = []
    closed_set = set()
    
    start_node = PuzzleNode(initial_state)
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return reconstruct_path(current_node)
        
        closed_set.add(tuple(map(tuple, current_node.state)))
        
        for neighbor_state, action, cost in get_neighbors(current_node.state):
            if tuple(map(tuple, neighbor_state)) not in closed_set:
                neighbor_node = PuzzleNode(neighbor_state, current_node, action, cost)
                heapq.heappush(open_list, neighbor_node)

    return None

def get_neighbors(state):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    blank_i, blank_j = find_blank(state)
    
    for dx, dy in directions:
        new_i, new_j = blank_i + dx, blank_j + dy
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = copy.deepcopy(state)
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            action = (dx, dy)
            cost = 1
            neighbors.append((new_state, action, cost))
    
    return neighbors

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def reconstruct_path(node):
    path = []
    while node.parent:
        path.insert(0, node.action)
        node = node.parent
    return path

def print_puzzle(state):
    for row in state:
        print(row)

if __name__ == "__main__":
    initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    
    solution = a_star(initial_state)
    if solution:
        print("Solution found:")
        current_state = initial_state
        for i, (dx, dy) in enumerate(solution):
            print(f"Step {i + 1}:")
            blank_i, blank_j = find_blank(current_state)
            new_i, new_j = blank_i + dx, blank_j + dy
            current_state[blank_i][blank_j], current_state[new_i][new_j] = current_state[new_i][new_j], current_state[blank_i][blank_j]
            print_puzzle(current_state)
            print()
    else:
        print("No solution found.")
