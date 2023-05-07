def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    h = 0
    for i in range(N-1):
        if A[i] <= h:
            break
        h = A[i] - h
    print(h)
