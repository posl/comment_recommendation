def search(start, visited, time):
    if time == k:
        return 1
    else:
        total = 0
        for i in range(n):
            if i != start and visited[i] == False:
                visited[i] = True
                total += search(i, visited, time + t[start][i])
                visited[i] = False
    return total
n, k = map(int, input().split())
t = [list(map(int, input().split())) for i in range(n)]
visited = [False for i in range(n)]
visited[0] = True
print(search(0, visited, 0))
