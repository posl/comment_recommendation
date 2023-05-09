def main():
    from sys import stdin
    from collections import deque
    N = int(stdin.readline().rstrip())
    E = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, stdin.readline().rstrip().split())
        E[u].append((v, w))
        E[v].append((u, w))
    D = [0] * (N + 1)
    Q = deque()
    Q.append(1)
    while Q:
        n = Q.popleft()
        for v, w in E[n]:
            if D[v] != 0:
                continue
            D[v] = D[n] + w
            Q.append(v)
    print('
'.join(map(lambda x: str(x % 2), D[1:])))
main()
