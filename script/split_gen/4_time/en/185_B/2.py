def main():
    N, M, T = map(int, input().split())
    A, B = [], []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = [0] + A + [T]
    B = [0] + B + [T]
    charge = N
    for i in range(M+1):
        charge -= A[i+1] - B[i]
        if charge <= 0:
            print("No")
            return
        charge += B[i+1] - A[i+1]
        if charge > N:
            charge = N
    print("Yes")
