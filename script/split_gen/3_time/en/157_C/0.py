def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
        elif S[0] == 1:
            print(C[0])
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(10, 11, sep='
')
        elif M == 1:
            if S[0] == 1:
                print(10 + C[0])
            elif S[0] == 2:
                print(10 * C[0])
            else:
                print(-1)
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                print(10 * C[0] + C[1])
            elif S[0] == 2 and S[1] == 1:
                print(10 * C[1] + C[0])
            else:
                print(-1)
        else:
            print(-1)
    else:
        if M == 0:
            print(100, 101, 102, 103, 104, 105, 106, 107, 108, 109, sep='
')
        elif M == 1:
            if S[0] == 1:
                print(100 + C[0])
            elif S[0] == 2:
                print(10 * C[0] + 0)
            elif S[0] == 3:
                print(1 * C[0] + 0)
            else:
                print(-1)
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                print(100 + 10 * C[0] + C[1])
            elif S[0] == 1 and S[1] == 3:
                print(100 + 1 * C[0] + C[1])
            elif S[0] == 2 and S[1] == 1:
                print(10 * C[1] + 0 + C[0
