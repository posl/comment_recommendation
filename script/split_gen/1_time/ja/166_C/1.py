def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    ans = 0
    for i in range(N):
        ok = True
        for j in G[i]:
            if H[i] <= H[j]:
                ok = False
                break
        if ok:
            ans += 1
    print(ans)
