def solve(N, L, R, A):
    #print("N, L, R, A", N, L, R, A)
    #print("A", A)
    #print("A[0:N//2]", A[0:N//2])
    #print("A[N//2:N]", A[N//2:N])
    #print("A[N//2:N][::-1]", A[N//2:N][::-1])
    if N == 1:
        if L > 0:
            return L + A[0]
        else:
            return A[0]
    else:
        if L > 0:
            if N % 2 == 0:
                return L + sum(A[0:N//2]) + R + sum(A[N//2:N][::-1])
            else:
                return L + sum(A[0:N//2]) + R + sum(A[N//2:N][::-1]) + A[N//2]
        else:
            if N % 2 == 0:
                return sum(A[0:N//2]) + R + sum(A[N//2:N][::-1])
            else:
                return sum(A[0:N//2]) + R + sum(A[N//2:N][::-1]) + A[N//2]

if __name__ == '__main__':
    solve()