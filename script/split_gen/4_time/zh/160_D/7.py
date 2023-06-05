def find_shortest_path(n, x, y):
    shortest_path = [0 for i in range(n)]
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if i <= x and j <= x:
                shortest_path[j-i] += 1
            elif i <= x and x < j < y:
                shortest_path[min(j-i, x-i+y-j)] += 1
            elif i <= x and j >= y:
                shortest_path[min(j-i, j-y+x-i)] += 1
            elif x < i < y and j >= y:
                shortest_path[min(j-i, j-y+x-i)] += 1
            elif x < i < y and x < j < y:
                shortest_path[min(j-i, x-i+y-j)] += 1
            elif x < i < y and j <= x:
                shortest_path[x-i+y-j] += 1
            elif i >= y and j >= y:
                shortest_path[j-i] += 1
            elif i >= y and x < j < y:
                shortest_path[x-i+y-j] += 1
            elif i >= y and j <= x:
                shortest_path[x-i+y-j] += 1
    return shortest_path
