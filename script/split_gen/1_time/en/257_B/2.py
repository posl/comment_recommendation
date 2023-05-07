def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    ans = [0] * K
    for i in range(K):
        ans[i] = A[i]
    for i in range(Q):
        if ans[L[i] - 1] != N:
            ans[L[i] - 1] += 1
    for i in range(K):
        print(ans[i], end=' ')
