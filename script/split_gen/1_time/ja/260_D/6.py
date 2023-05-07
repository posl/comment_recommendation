def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    PQ = [(-1, -1) for _ in range(N + 1)]
    for i in range(N):
        PQ[P[i]] = (i, -1)
    for i in range(N):
        PQ[P[i]] = (PQ[P[i]][0], i)
    PQ = PQ[1:]
    PQ.sort(key=lambda x: x[0])
    ans = [-1 for _ in range(N)]
    for i in range(N):
        if PQ[i][1] - PQ[i][0] >= K - 1:
            ans[PQ[i][1]] = PQ[i][1] + 1
    for i in range(N):
        if ans[i] == -1:
            continue
        for j in range(i + 1, N):
            if ans[j] == -1:
                if PQ[j][1] - PQ[i][1] >= K:
                    ans[j] = ans[i]
                else:
                    break
            else:
                break
    for i in range(N):
        print(ans[i])
