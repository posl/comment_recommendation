def main():
    N, M = map(int,input().split())
    X = list(map(int,input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int,input().split())
    ans = 0
    for i in range(N):
        ans += X[i]
        for j in range(M):
            if i + 1 == C[j]:
                ans += Y[j]
    print(ans)
