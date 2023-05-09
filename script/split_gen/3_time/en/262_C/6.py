def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for i in range(N-1):
        if A[i] == i+1:
            ans += 1
        elif A[i] < i+1 and A[i+1] > i+1:
            ans += 1
    if A[N-1] == N:
        ans += 1
    print(ans)
