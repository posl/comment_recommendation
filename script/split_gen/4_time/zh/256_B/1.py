def main():
    N = int(input())
    A = input().split()
    P = 0
    for i in range(N):
        A[i] = int(A[i])
        P += A[i]//4
        if A[i]%4 == 0:
            A[i] = 0
        else:
            A[i] = 4 - A[i]%4
    print(P)
