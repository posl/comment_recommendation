def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] % 2 == 1:
        print(-1)
        return
    if A[-1] == A[-2]:
        print(A[-1])
        return
    if A[-1] == A[-2] + 1:
        print(-1)
        return
    print(A[-1])
