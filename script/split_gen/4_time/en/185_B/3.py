def main():
    N, M, T = map(int, input().split())
    A = [0] * (M + 1)
    B = [0] * (M + 1)
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A[M] = T
    B[M] = T
    charge = N
    for i in range(M + 1):
        charge -= (A[i] - B[i - 1])
        if charge <= 0:
            print('No')
            return
        charge += (B[i] - A[i])
        if charge > N:
            charge = N
    print('Yes')
