def max_orange(N, A):
    max_orange = 0
    for l in range(1, N+1):
        for r in range(l, N+1):
            for x in range(1, max(A[l-1:r])):
                if x <= A[l-1:r].min():
                    max_orange = max(max_orange, x*(r-l+1))
    return max_orange
N = 6
A = [2, 4, 4, 9, 4, 9]
print(max_orange(N, A))
N = 6
A = [200, 4, 4, 9, 4, 9]
print(max_orange(N, A))
