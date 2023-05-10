def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N-1):
        if A[i] <= A[i+1]:
            ans += 1
        else:
            ans = 0
    print(ans+1)
