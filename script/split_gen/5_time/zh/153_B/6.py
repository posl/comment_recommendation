def solve(H, A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                return 'Yes'
    return 'No'
H, N = map(int, input().split())
A = list(map(int, input().split()))
print(solve(H, A))
