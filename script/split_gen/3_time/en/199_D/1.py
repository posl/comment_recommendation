def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    if M == 0:
        print(3**N)
        return
    ans = 0
    for i in range(N):
        for j in G[i]:
            if i > j:
                continue
            for k in G[j]:
                if i > k or j > k:
                    continue
                if i in G[k] or j in G[k]:
                    continue
                ans += 6
    print(ans)
