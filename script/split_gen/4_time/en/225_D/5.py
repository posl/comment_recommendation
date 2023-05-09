def main():
    N, Q = map(int, input().split())
    # List of queries
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    # List of cars
    cars = [i for i in range(1, N+1)]
    # List of connected components
    components = [[i] for i in range(1, N+1)]
    # List of car numbers of the front of connected components
    front = [i for i in range(1, N+1)]
    # List of car numbers of the rear of connected components
    rear = [i for i in range(1, N+1)]
    # List of car numbers of the rear of connected components
    rear = [i for i in range(1, N+1)]
    # Dictionary of car numbers of the front of connected components
    front_dict = {i: i for i in range(1, N+1)}
    # Dictionary of car numbers of the rear of connected components
    rear_dict = {i: i for i in range(1, N+1)}
    # Process each query
    for query in queries:
        # If query is type 1
        if query[0] == 1:
            # Get the car numbers
            x = query[1]
            y = query[2]
            # Get the front and rear of connected components
            front_x = front_dict[x]
            front_y = front_dict[y]
            rear_x = rear_dict[x]
            rear_y = rear_dict[y]
            # Get the index of connected components
            index_x = front.index(front_x)
            index_y = front.index(front_y)
            # Merge connected components
            components[index_x] = components[index_x] + components[index_y]
            # Update the front and rear of connected components
            front[index_x] = front_x
            rear[index_x] = rear_y
            # Update the front and rear of connected components
            front_dict[front_x] = front_x
            rear_dict[rear_y] = rear_y
            # Delete the front and rear of connected components
            front.pop(index_y)
            rear.pop(index_y)
            # Delete the front and rear of connected components
            del front_dict[front_y]
            del rear_dict[rear_y]
            # Delete the connected
