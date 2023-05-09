def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = [A[i], i]
    B.sort()
    ans = [K // N] * N
    K %= N
    for i in range(K):
        ans[B[i][1]] += 1
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    solve()