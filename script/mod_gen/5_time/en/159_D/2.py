def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[A[i]-1] += 1
    for i in range(N):
        print(ans[i])
    return 0

if __name__ == '__main__':
    solve()