def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    ans = [0] * N
    for i in range(Q):
        ans[A[i] - 1] += 1
    for i in range(N):
        if K - Q + ans[i] > 0:
            print('Yes')
        else:
            print('No')
