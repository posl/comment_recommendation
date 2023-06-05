def find_second_place(N, A):
    if N == 1:
        return 1 if A[0] < A[1] else 2
    if N == 2:
        return 1 if A[0] > A[2] else 2
    if N == 3:
        return 1 if A[0] > A[4] else 2
    if N == 4:
        return 1 if A[0] > A[8] else 2
    if N == 5:
        return 1 if A[0] > A[16] else 2
    if N == 6:
        return 1 if A[0] > A[32] else 2
    if N == 7:
        return 1 if A[0] > A[64] else 2
    if N == 8:
        return 1 if A[0] > A[128] else 2
    if N == 9:
        return 1 if A[0] > A[256] else 2
    if N == 10:
        return 1 if A[0] > A[512] else 2
    if N == 11:
        return 1 if A[0] > A[1024] else 2
    if N == 12:
        return 1 if A[0] > A[2048] else 2
    if N == 13:
        return 1 if A[0] > A[4096] else 2
    if N == 14:
        return 1 if A[0] > A[8192] else 2
    if N == 15:
        return 1 if A[0] > A[16384] else 2
    if N == 16:
        return 1 if A[0] > A[32768] else 2
