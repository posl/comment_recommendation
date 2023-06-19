def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    # print(A)
    def calc(K):
        # print("K:", K)
        if N == 1:
            return 1 if A[0] == K else 0
        if N == 2:
            return 1 if ((A[0] + A[1]) % 10 == K) else 0
        if N == 3:
            return 1 if (((A[0] + A[1]) % 10) * A[2]) % 10 == K else 0
        if N == 4:
            return 1 if (((A[0] + A[1]) % 10) * ((A[2] + A[3]) % 10)) % 10 == K else 0
        if N == 5:
            return 1 if (((A[0] + A[1]) % 10) * ((A[2] + A[3]) % 10) * A[4]) % 10 == K else 0
        if N == 6:
            return 1 if (((A[0] + A[1]) % 10) * ((A[2] + A[3]) % 10) * ((A[4] + A[5]) % 10)) % 10 == K else 0
        if N == 7:
            return 1 if (((A[0] + A[1]) % 10) * ((A[2] + A[3]) % 10) * ((A[4] + A[5]) % 10) * A[6]) % 10 == K else 0
        if N == 8:
            return 1 if (((A[0] + A[1]) % 10) * ((A[2] + A[3]) % 10) * ((A[4] + A[5]) % 10) * ((A[6] + A[7]) % 10)) % 10 == K else 0
        if N == 9:
            return 1 if (((A[0] + A[1]) % 10) * ((A[2] + A[3]) % 10) * ((A[4
