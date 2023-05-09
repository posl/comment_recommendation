def main():
    N, M = map(int, input().split())
    if M == 0:
        print(3**N)
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = 0
    for i in range(3**N):
        col = [0] * N
        for j in range(N):
            col[j] = (i // (3**j)) % 3
        ok = True
        for j in range(N):
            for k in G[j]:
                if col[j] == col[k]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            ans += 1
    print(ans)
