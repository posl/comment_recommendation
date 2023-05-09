def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    for i in range(N):
        ans[i] = K // N
        if i < K % N:
            ans[i] += 1
    for i in range(N):
        if A[i] <= K % N:
            ans[i] -= 1
    print(*ans, sep="\n")
solve()

if __name__ == '__main__':
    solve()