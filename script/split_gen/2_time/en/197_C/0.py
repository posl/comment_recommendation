def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(A[0])
        return
    if N == 2:
        print(A[0] ^ A[1])
        return
    if N == 3:
        print(A[0] ^ A[1] ^ A[2])
        return
    if N == 4:
        print(A[0] ^ A[1] ^ A[2] ^ A[3])
        return
    if N == 5:
        print(A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4])
        return
    if N == 6:
        print(A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4] ^ A[5])
        return
    if N == 7:
        print(A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4] ^ A[5] ^ A[6])
        return
    if N == 8:
        print(A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4] ^ A[5] ^ A[6] ^ A[7])
        return
    if N == 9:
        print(A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4] ^ A[5] ^ A[6] ^ A[7] ^ A[8])
        return
    if N == 10:
        print(A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4] ^ A[5] ^ A[6] ^ A[7] ^ A[8] ^ A[9])
        return
    if N == 11:
        print(A[0] ^ A[1] ^ A[2] ^ A[3] ^ A[4] ^ A[5] ^ A[6] ^ A[7] ^ A[8] ^ A[9] ^ A[10])
        return
    if N == 12:
        print(A[0] ^ A[1] ^ A[2] ^ A[3] ^ A
