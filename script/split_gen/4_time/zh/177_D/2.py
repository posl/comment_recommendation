def main():
    N, M = map(int, input().split())
    friends = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a - 1].append(b - 1)
        friends[b - 1].append(a - 1)
    colors = [-1] * N
    colors[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u in friends[v]:
            if colors[u] == -1:
                colors[u] = 1 - colors[v]
                stack.append(u)
            elif colors[u] == colors[v]:
                print(-1)
                return
    print(colors.count(0), colors.count(1))
