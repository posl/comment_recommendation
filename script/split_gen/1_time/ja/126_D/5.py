def main():
    N = int(input())
    E = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        E[u].append((v, w))
        E[v].append((u, w))
    C = [-1] * (N + 1)
    C[1] = 0
    Q = [1]
    while Q:
        x = Q.pop()
        for y, w in E[x]:
            if C[y] == -1:
                C[y] = C[x] ^ (w % 2)
                Q.append(y)
    for i in range(1, N + 1):
        print(C[i])
