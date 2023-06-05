def solve():
    N = int(input())
    A = list(map(int,input().split()))
    # N = 3
    # A = [2,7,6]
    ans = [0]*10
    for i in range(10):
        if i == A[-1]:
            ans[i] = 1
    for i in range(N-2,-1,-1):
        new = [0]*10
        for j in range(10):
            if (j+A[i])%10 == A[i+1]:
                new[j] += ans[j]
            if (j*A[i])%10 == A[i+1]:
                new[j] += ans[j]
        ans = new
    for i in range(10):
        print(ans[i])
solve()
