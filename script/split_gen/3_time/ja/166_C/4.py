def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    H.insert(0, 0)
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    ans = 0
    for i in range(1, N+1):
        flag = True
        for j in G[i]:
            if H[i] <= H[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
