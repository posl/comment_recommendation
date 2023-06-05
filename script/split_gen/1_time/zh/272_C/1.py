def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == 0:
        print(-1)
    else:
        print(A[-1] + A[-2])
