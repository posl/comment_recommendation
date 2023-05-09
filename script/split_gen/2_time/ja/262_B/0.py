def main():
    N, M = map(int, input().split())
    U = []
    V = []
    for i in range(M):
        u, v = map(int, input().split())
        U.append(u)
        V.append(v)
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            if U[i] == U[j] or U[i] == V[j] or V[i] == U[j] or V[i] == V[j]:
                continue
            for k in range(j+1, M):
                if U[i] == U[k] or U[i] == V[k] or V[i] == U[k] or V[i] == V[k]:
                    continue
                if U[i] == U[j] or U[i] == V[j] or V[i] == U[j] or V[i] == V[j]:
                    continue
                ans += 1
    print(ans)
