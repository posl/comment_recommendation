def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = sorted(A)
    B = sorted(B)
    C = []
    D = []
    for i in range(N):
        if i == 0:
            C.append(A[i])
            D.append(B[i])
        else:
            if A[i] != A[i-1]:
                C.append(A[i])
            if B[i] != B[i-1]:
                D.append(B[i])
    for i in range(N):
        print(C.index(A[i])+1, D.index(B[i])+1)
