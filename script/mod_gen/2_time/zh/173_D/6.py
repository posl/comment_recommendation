def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    ans = 0
    sum = 0
    for i in range(2*N):
        sum += A[i]
        if i >= N:
            sum -= A[i-N]
        if i >= N-1:
            ans = max(ans, sum)
    print(ans)
solve()
