def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2 * N + 1)
    for i in range(N):
        ans[A[i]] = i + 1
    for i in range(1, N + 1):
        print(0)
        print(ans[i])
        print(ans[i])
        print(ans[2 * i])
        print(ans[2 * i + 1])
solve()

if __name__ == '__main__':
    solve()