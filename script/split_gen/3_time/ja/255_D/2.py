def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    ans = [0] * Q
    for i in range(N):
        for j in range(Q):
            ans[j] += abs(A[i] - X[j])
    print('
'.join(map(str, ans)))
