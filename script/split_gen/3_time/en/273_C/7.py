def solve(N, A):
    A = sorted(A)
    ans = []
    for i in range(N):
        if i == 0:
            ans.append(N - A[::-1].index(A[i]) - 1)
        elif i == N - 1:
            ans.append(A.index(A[i]))
        else:
            ans.append(N - A[::-1].index(A[i]) - 1 - A.index(A[i]))
    return ans
