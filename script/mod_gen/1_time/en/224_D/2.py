def main():
    M = int(input())
    E = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    G = [[] for _ in range(9)]
    for u, v in E:
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    def dfs(v, used, p):
        if used[v]:
            return False
        used[v] = True
        if v == 8:
            return True
        for u in G[v]:
            if p[u] == p[v] + 1 and dfs(u, used, p):
                return True
        return False
    def solve(p):
        used = [False] * 9
        return dfs(0, used, p)
    if solve(P):
        print(0)
        return
    for i in range(8):
        for j in range(i + 1, 8):
            P[i], P[j] = P[j], P[i]
            if solve(P):
                print(1)
                return
            P[i], P[j] = P[j], P[i]
    print(2)

if __name__ == '__main__':
    main()