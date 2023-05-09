def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0]*N
    ans[0] = sum(A)
    for i in range(N-1):
        ans[0] -= 2*A[i+1]
    for i in range(N-1):
        ans[i+1] = 2*A[i] - ans[i]
    print(*ans)

if __name__ == '__main__':
    solve()