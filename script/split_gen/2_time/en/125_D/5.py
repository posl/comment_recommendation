def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] * (-1) ** i
    C = [0] * N
    for i in range(N):
        C[i] = B[i] * (-1) ** i
    D = [0] * N
    for i in range(N):
        D[i] = C[i] * (-1) ** i
    sumB = sum(B)
    sumC = sum(C)
    sumD = sum(D)
    if sumB >= 0 and sumC >= 0 and sumD >= 0:
        print(sumB)
    elif sumB <= 0 and sumC >= 0 and sumD >= 0:
        print(sumC)
    elif sumB <= 0 and sumC <= 0 and sumD >= 0:
        print(sumD)
    elif sumB <= 0 and sumC <= 0 and sumD <= 0:
        print(sumB)
    else:
        pass
