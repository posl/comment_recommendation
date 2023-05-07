def main():
    N, M = map(int, input().split())
    if N == 2:
        print(0)
        return
    E = [set() for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        E[u].add(v)
        E[v].add(u)
    ans = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if j not in E[i]:
                ans += 1
    print(ans)
