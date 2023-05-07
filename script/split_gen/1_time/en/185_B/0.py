def main():
    N, M, T = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    charge = N
    for i in range(M):
        charge -= A[i] - (0 if i == 0 else B[i - 1])
        if charge <= 0:
            print("No")
            return
        charge += B[i] - A[i]
        if charge >= N:
            charge = N
    charge -= T - B[M - 1]
    if charge <= 0:
        print("No")
        return
    print("Yes")
