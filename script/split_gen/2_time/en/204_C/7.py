def main():
    N, M = map(int, input().split())
    road = []
    for i in range(M):
        A, B = map(int, input().split())
        road.append([A, B])
    if M == 0:
        print(N**2)
        return
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                ans += 1
                continue
            visited = [0]*(N+1)
            visited[i+1] = 1
            visited[j+1] = 1
            stack = [i+1]
            while len(stack) > 0:
                x = stack.pop()
                for k in range(M):
                    if road[k][0] == x and visited[road[k][1]] == 0:
                        stack.append(road[k][1])
                        visited[road[k][1]] = 1
                    if road[k][1] == x and visited[road[k][0]] == 0:
                        stack.append(road[k][0])
                        visited[road[k][0]] = 1
            ans += sum(visited)
    print(ans)
