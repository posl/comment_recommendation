def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    print(A)
    P = 0
    for i in range(N):
        P += A[i]
        if P >= 4:
            P = P - 4
    print(P)
