def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    B = [A[i+1] - A[i] for i in range(N-1)]
    ans = 0
    for i in range(N-1):
        ans += abs(B[i])
    for i in range(Q):
        if i != 0:
            ans -= abs(B[X[i]-2])
            B[X[i]-2] += B[X[i]-1]
            ans += abs(B[X[i]-2])
        if i != Q-1:
            ans -= abs(B[X[i]-1])
            B[X[i]-1] += B[X[i]-2]
            ans += abs(B[X[i]-1])
        print(ans)
