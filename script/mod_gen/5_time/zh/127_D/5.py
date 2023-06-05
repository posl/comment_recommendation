def solve(N, M, A, BC):
    A.sort(reverse=True)
    BC.sort(key=lambda x:x[1], reverse=True)
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
        else:
            break
        i += 1
    return sum(A)

if __name__ == '__main__':
    solve()