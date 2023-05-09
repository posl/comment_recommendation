def main():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    charge = N
    for i in range(M):
        charge -= A[i] - (0 if i == 0 else B[i-1])
        if charge <= 0:
            print("No")
            return
        charge += B[i] - A[i]
        if charge >= N:
            charge = N
    charge -= T - B[-1]
    if charge <= 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()