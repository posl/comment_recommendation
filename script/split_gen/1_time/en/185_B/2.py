def main():
    N, M, T = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    charge = N
    for i in range(M):
        charge -= A[i]
        if charge <= 0:
            print("No")
            return
        charge += B[i] - A[i]
        if charge > N:
            charge = N
    charge -= T - B[-1]
    if charge <= 0:
        print("No")
    else:
        print("Yes")
