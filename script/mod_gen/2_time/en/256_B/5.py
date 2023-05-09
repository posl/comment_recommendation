def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P = 0
        else:
            P = P + A[i-1]
        if P >= 4:
            P = P - 4
        if P == 0:
            if A[i] == 1:
                P = P + 1
            elif A[i] == 2:
                P = P + 2
            elif A[i] == 3:
                P = P + 3
            elif A[i] == 4:
                P = P + 4
        elif P == 1:
            if A[i] == 1:
                P = P + 1
            elif A[i] == 2:
                P = P + 2
            elif A[i] == 3:
                P = P + 3
            elif A[i] == 4:
                P = P + 4
        elif P == 2:
            if A[i] == 1:
                P = P + 1
            elif A[i] == 2:
                P = P + 2
            elif A[i] == 3:
                P = P + 3
            elif A[i] == 4:
                P = P + 4
        elif P == 3:
            if A[i] == 1:
                P = P + 1
            elif A[i] == 2:
                P = P + 2
            elif A[i] == 3:
                P = P + 3
            elif A[i] == 4:
                P = P + 4
    print(P)

if __name__ == '__main__':
    main()