def main():
    N = int(input())
    V = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        V[u - 1].append((v - 1, w))
        V[v - 1].append((u - 1, w))
    #print(V)
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u, w in V[v]:
            if color[u] == -1:
                color[u] = (color[v] + w) % 2
                stack.append(u)
    for c in color:
        print(c)
