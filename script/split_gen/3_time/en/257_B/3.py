def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = [int(input()) for _ in range(Q)]
    S = [0] * N
    for i in range(Q):
        S[L[i] - 1] += 1
    for i in range(N):
        if K - Q + S[i] > 0:
            print('Yes')
        else:
            print('No')
