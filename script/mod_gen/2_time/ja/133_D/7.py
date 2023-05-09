def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0]*N
    for i in range(N):
        ans[i] = ((A[i-1] + A[i])//2)
    print(*ans)

if __name__ == '__main__':
    solve()