def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    for i in range(Q):
        ans = 0
        for j in range(N):
            ans += abs(A[j] - X[i])
        print(ans)
