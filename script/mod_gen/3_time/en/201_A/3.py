def arithmetic_sequence(A):
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        return "Yes"
    else:
        return "No"
A = list(map(int, input().split()))
print(arithmetic_sequence(A))
