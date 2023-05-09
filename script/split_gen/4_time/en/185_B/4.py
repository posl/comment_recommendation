def main():
    N, M, T = map(int, input().split())
    A = [0]
    B = [0]
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.append(T)
    B.append(T)
    charge = N
    for i in range(M+1):
        charge -= (A[i+1] - B[i])
        if charge <= 0:
            print("No")
            return
        charge += (B[i+1] - A[i+1])
        if charge > N:
            charge = N
    print("Yes")
