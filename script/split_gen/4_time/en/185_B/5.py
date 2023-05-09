def main():
    N, M, T = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    charge = N
    for i in range(M):
        if i == 0:
            charge -= A[i]
            if charge <= 0:
                print('No')
                return
        else:
            charge -= A[i] - B[i-1]
            if charge <= 0:
                print('No')
                return
        charge += B[i] - A[i]
        if charge > N:
            charge = N
    charge -= T - B[-1]
    if charge <= 0:
        print('No')
        return
    print('Yes')
