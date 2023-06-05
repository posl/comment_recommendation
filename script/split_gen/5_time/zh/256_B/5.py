def main():
    N = int(input())
    A = input().split()
    P = 0
    for i in range(N):
        A[i] = int(A[i])
        P = P + A[i] // 4
        A[i] = A[i] % 4
    for i in range(N):
        if A[i] == 1:
            P = P + 1
        elif A[i] == 2:
            P = P + 2
        elif A[i] == 3:
            P = P + 1
    print(P)
