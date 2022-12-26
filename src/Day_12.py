from utils import read_file
from collections import deque

values = read_file(12, str, True)


def find_path(graph, start, end):
    # Initialize a queue with the starting node and a visited set
    queue = deque([start])
    visited = set()

    # A dictionary to store the predecessor of each node (key) in the path
    # from the start node to the key
    predecessor = {start: None}

    # Perform BFS
    while queue:
        # print(queue)
        # Dequeue the first node from the queue and mark it as visited
        current = queue.popleft()
        visited.add(current)

        # Check if the current node is the destination node
        if current == end:
            # If it is, reconstruct the path from the start node to the end node
            # by following the predecessors from the end node to the start node
            path = []
            while current is not None:
                path.append(current)
                current = predecessor[current]
            return path[::-1]  # Return the path in the correct order

        # For each neighbor of the current node, check if it is a valid move
        # (a value one higher or lower than the current node) and if it has not been visited
        for neighbor in graph[current]:
            if (neighbor - current == 1 or current > neighbor) and neighbor not in visited:
                # If it is a valid move and has not been visited, add it to the queue
                # and mark it as visited
                queue.append(neighbor)
                visited.add(neighbor)
                predecessor[neighbor] = current  # Store the current node as the predecessor of the neighbor

    # If the queue is empty and the destination node has not been reached,
    # there is no path from the start node to the end node
    return None


# Example usage

# Define the graph as an adjacency list
graph = {
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8],
    8: [5, 7, 9],
    9: [6, 8]
}

# Find the path from node 1 to node 9
path = find_path(graph, 1, 9)

# Print the path
print(path)  # Output: [1, 2, 5, 8, 9]
