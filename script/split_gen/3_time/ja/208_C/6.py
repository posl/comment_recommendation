def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    a = sorted(A)
    ans = [0] * N
    for i in range(N):
        ans[i] = K // N
        if K % N > i:
            ans[i] += 1
    for i in range(N):
        ans[A.index(a[i])] += ans[i]
        ans[i] = 0
    for i in range(N):
        print(ans[i])
