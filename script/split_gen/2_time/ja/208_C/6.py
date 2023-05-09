def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [10**9+1]
    ans = [0] * N
    for i in range(N):
        if A[i+1] - A[i] > 0:
            ans[i] = (A[i+1] - A[i]) * ((i+1) * K // N) - K
            K -= ans[i]
    for i in range(N):
        print(ans[i] // (i+1) + K // N + 1)
