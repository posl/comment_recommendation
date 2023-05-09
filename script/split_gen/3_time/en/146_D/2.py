def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = [0] * (N-1)
    color = 1
    for v in range(N):
        used = [0] * (N+1)
        for u in G[v]:
            used[ans[u]] = 1
        for u in G[v]:
            if ans[u] == 0:
                for i in range(1, N+1):
                    if used[i] == 0:
                        ans[u] = i
                        used[i] = 1
                        break
    print(max(ans))
    for a in ans:
        print(a)
    return
