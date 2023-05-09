def main():
    N, M, T = map(int, input().split())
    A, B = [], []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.append(T)
    B.append(T)
    now = 0
    for i in range(M+1):
        N -= A[i] - now
        if N <= 0:
            print("No")
            return
        N += B[i] - A[i]
        if N >= N:
            N = N
        now = B[i]
    print("Yes")
