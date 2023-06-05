def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == A[1]:
        return A[-1]
    else:
        return A[0]
print(solve())
