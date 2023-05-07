def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    for p in P:
        p.sort()
    P.sort(key=lambda x: x[0])
    for i in range(N):
        if i < K - 1 or P[i][0] + P[i][1] + P[i][2] + P[i][3] >= P[K - 1][0] + P[K - 1][1] + P[K - 1][2] + P[K - 1][3]:
            print("Yes")
        else:
            print("No")
