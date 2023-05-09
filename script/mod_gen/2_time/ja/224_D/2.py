def main():
    M = int(input())
    G = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    P = [int(x) - 1 for x in input().split()]
    ans = 10**9
    for i in range(9):
        if i in P:
            continue
        for j in range(len(G[i])):
            if G[i][j] in P:
                ans = min(ans, 1)
                break
            for k in range(len(G[G[i][j]])):
                if G[G[i][j]][k] in P:
                    ans = min(ans, 2)
                    break
            if ans == 2:
                break
        if ans == 1:
            break
    if ans == 10**9:
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()