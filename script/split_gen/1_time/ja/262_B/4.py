def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        E[u-1].append(v-1)
        E[v-1].append(u-1)
    ans = 0
    for a in range(N):
        for b in E[a]:
            if a >= b:
                continue
            for c in E[b]:
                if a >= c or b >= c:
                    continue
                if c in E[a]:
                    ans += 1
    print(ans)
