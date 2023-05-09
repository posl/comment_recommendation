def main():
    N, M = map(int, input().split())
    if M == 0:
        print(3**N)
        return
    edges = [[0]*N for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a-1][b-1] = 1
        edges[b-1][a-1] = 1
    ans = 0
    for i in range(3**N):
        i = str(i).zfill(N)
        ok = True
        for j in range(N):
            for k in range(j+1, N):
                if i[j] == i[k] and edges[j][k] == 1:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            ans += 1
    print(ans)
