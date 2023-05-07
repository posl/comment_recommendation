def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    for i in range(N):
        if K >= N:
            ans[i] += 1
            K -= 1
        else:
            ans[A.index(A[i])] += K // N
            K %= N
    for i in range(N):
        print(ans[i])
