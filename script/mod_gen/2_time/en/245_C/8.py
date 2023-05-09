def solve(N, K, A, B):
    if N == 1:
        return 'Yes'
    if N == 2:
        if abs(A[0] - A[1]) <= K or abs(B[0] - B[1]) <= K or abs(A[0] - B[1]) <= K or abs(B[0] - A[1]) <= K:
            return 'Yes'
        else:
            return 'No'
    if N == 3:
        if abs(A[0] - A[1]) <= K or abs(B[0] - B[1]) <= K:
            if abs(A[1] - A[2]) <= K or abs(B[1] - B[2]) <= K:
                return 'Yes'
        if abs(A[0] - A[2]) <= K or abs(B[0] - B[2]) <= K:
            if abs(A[1] - A[2]) <= K or abs(B[1] - B[2]) <= K:
                return 'Yes'
        if abs(A[0] - B[1]) <= K or abs(B[0] - A[1]) <= K:
            if abs(A[1] - B[2]) <= K or abs(B[1] - A[2]) <= K:
                return 'Yes'
        if abs(A[0] - B[2]) <= K or abs(B[0] - A[2]) <= K:
            if abs(A[1] - B[2]) <= K or abs(B[1] - A[2]) <= K:
                return 'Yes'
        return 'No'
    if N == 4:
        if abs(A[0] - A[1]) <= K or abs(B[0] - B[1]) <= K:
            if abs(A[1] - A[2]) <= K or abs(B[1] - B[2]) <= K:
                if abs(A[2] - A[3]) <= K or abs(B[2] - B[3]) <= K:
                    return 'Yes'
        if abs(A[0] - A[2]) <= K or abs(B[0] - B[2]) <= K:
            if abs(A[1] - A[2]) <= K or abs(B[1] - B[2])

if __name__ == '__main__':
    solve()