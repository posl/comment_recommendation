def isPermutation(A):
    A.sort()
    for i in range(len(A)):
        if A[i] != i + 1:
            return "No"
    return "Yes"
N = int(input())
A = list(map(int,input().split()))
print(isPermutation(A))
