def solve():
    A = list(map(int, input().split()))
    A.sort()
    if A[0] + A[1] + A[2] >= A[3]:
        print(1)
    else:
        print(0)
