def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        if A[0] == 1:
            print(0)
        else:
            print(-1)
        return
    if max(A) == N:
        print(-1)
        return
    ans = 0
    for i in range(N-1):
        if A[i] == i+1:
            ans += 1
        else:
            break
    print(N-ans)
