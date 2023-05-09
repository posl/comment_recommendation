def solve(A):
    if len(A) == 1:
        return A[0]
    if len(A) == 2:
        return A[0] ^ A[1]
    if len(A) == 3:
        return A[0] ^ A[1] ^ A[2]
    if len(A) == 4:
        return A[0] ^ A[1] ^ A[2] ^ A[3]
    if len(A) == 5:
        return A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4]
    if len(A) == 6:
        return A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4] ^ A[5]
    if len(A) == 7:
        return A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4] ^ A[5] ^ A[6]
    if len(A) == 8:
        return A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4] ^ A[5] ^ A[6] ^ A[7]
    if len(A) == 9:
        return A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4] ^ A[5] ^ A[6] ^ A[7] ^ A[8]
    if len(A) == 10:
        return A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4] ^ A[5] ^ A[6] ^ A[7] ^ A[8] ^ A[9]
    if len(A) == 11:
        return A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4] ^ A[5] ^ A[6] ^ A[7] ^ A[8] ^ A[9] ^ A[10]
    if len(A) == 12:
        return A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4] ^ A[6] ^ A[7] ^ A[8] ^ A[9] ^ A

if __name__ == '__main__':
    solve()