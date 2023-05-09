def main():
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        E[a - 1].append(b - 1)
        E[b - 1].append(a - 1)
    ans = 0
    for i in range(N):
        if E[i] == []:
            ans += 1
            continue
        v = [False] * N
        v[i] = True
        q = [i]
        while q:
            w = q.pop()
            for e in E[w]:
                if not v[e]:
                    v[e] = True
                    q.append(e)
        if not all(v):
            ans += 1
    print(ans)
