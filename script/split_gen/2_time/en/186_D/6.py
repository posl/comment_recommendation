def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(abs(A[0] - A[1]))
        return
    A.sort()
    L = A[:N//2]
    R = A[N//2:]
    Lsum = sum(L)
    Rsum = sum(R)
    Llen = len(L)
    Rlen = len(R)
    print((Rsum - Lsum) * 2 - R[0] + L[-1] + (Rlen - Llen) * (R[0] - L[-1]))
