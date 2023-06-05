def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0]*N
    for i in range(N):
        ans[i] = A.count(A[i])
    for i in range(N):
        print(ans[i]-1)
solve()
