def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    for i in range(N):
        ans[i] = len(set(A[i:]))
    print(*ans, sep='\n')
