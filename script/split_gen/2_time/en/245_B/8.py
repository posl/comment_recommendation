def solve():
    N = int(input())
    A = [int(a) for a in input().split()]
    A.sort()
    for i in range(N):
        if i != A[i]:
            return i
    return N
