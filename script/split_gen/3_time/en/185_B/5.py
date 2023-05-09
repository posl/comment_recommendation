def main():
    N,M,T = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        A_i,B_i = map(int,input().split())
        A.append(A_i)
        B.append(B_i)
    charge = N
    cafe = 0
    for i in range(M):
        charge = charge - (A[i] - cafe)
        if charge <= 0:
            print('No')
            return
        charge = charge + (B[i] - A[i])
        if charge > N:
            charge = N
        cafe = B[i]
    charge = charge - (T - cafe)
    if charge <= 0:
        print('No')
    else:
        print('Yes')
