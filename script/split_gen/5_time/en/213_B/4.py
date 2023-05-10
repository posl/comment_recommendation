def booby_prize():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = sorted(A, reverse=True)
    for i in range(N):
        if A[i] == B[1]:
            return i + 1
print(booby_prize())
