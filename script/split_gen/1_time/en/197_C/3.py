def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(0)
        return
    A.sort()
    if A[0] == A[-1]:
        print(0)
        return
    if A[0] == 0:
        print(0)
        return
    if N == 2:
        print(A[0] ^ A[1])
        return
    if N == 3:
        print(min(A[0] ^ A[1], A[1] ^ A[2]))
        return
    if N == 4:
        print(min(A[0] ^ A[1], A[1] ^ A[2], A[2] ^ A[3]))
        return
    if N == 5:
        print(min(A[0] ^ A[1], A[1] ^ A[2], A[2] ^ A[3], A[3] ^ A[4]))
        return
    if N == 6:
        print(min(A[0] ^ A[1], A[1] ^ A[2], A[2] ^ A[3], A[3] ^ A[4], A[4] ^ A[5]))
        return
    if N == 7:
        print(min(A[0] ^ A[1], A[1] ^ A[2], A[2] ^ A[3], A[3] ^ A[4], A[4] ^ A[5], A[5] ^ A[6]))
        return
    if N == 8:
        print(min(A[0] ^ A[1], A[1] ^ A[2], A[2] ^ A[3], A[3] ^ A[4], A[4] ^ A[5], A[5] ^ A[6], A[6] ^ A[7]))
        return
    if N == 9:
        print(min(A[0] ^ A[1], A[1] ^ A[2], A[2] ^ A[3], A[3] ^ A[4], A[4] ^ A[5], A[5] ^ A[6], A[6] ^ A[7], A[7] ^ A[8]))
