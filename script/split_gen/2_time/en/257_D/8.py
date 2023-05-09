def trampoline(n, trampolines):
    # Define the graph
    graph = [[0 for _ in range(n)] for _ in range(n)]
    # Fill the graph
    for i in range(n):
        for j in range(n):
            if i != j:
                if trampolines[i][2] * (i + 1) >= abs(trampolines[i][0] - trampolines[j][0]) + abs(trampolines[i][1] - trampolines[j][1]):
                    graph[i][j] = 1
    # Define the distance of each node from the starting node
    distance = [float('inf') for _ in range(n)]
    # Define the starting node
    start = 0
    # Define the visited nodes
    visited = [False for _ in range(n)]
    # Define the queue
    queue = []
    # Initialize the distance of the starting node
    distance[start] = 0
    # Add the starting node to the queue
    queue.append(start)
    # While the queue is not empty
    while queue:
        # Pop the first node from the queue
        node = queue.pop(0)
        # If the node is not visited
        if not visited[node]:
            # Mark the node as visited
            visited[node] = True
            # For each neighbor of the node
            for neighbor in range(n):
                # If the neighbor is not visited
                if not visited[neighbor]:
                    # If the distance of the neighbor is greater than the distance of the node plus the distance between the node and the neighbor
                    if distance[neighbor] > distance[node] + graph[node][neighbor]:
                        # Update the distance of the neighbor
                        distance[neighbor] = distance[node] + graph[node][neighbor]
                        # Add the neighbor to the queue
                        queue.append(neighbor)
    # Return the maximum distance
    return max(distance)
