def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    if N == 1:
        if M == 0:
            print(0)
        else:
            if S[0] == 1:
                print(C[0])
            else:
                print(-1)
        return
    if N == 2:
        if M == 0:
            print(10, 11, sep='
')
        else:
            if S[0] == 1:
                if C[0] == 0:
                    print(-1)
                else:
                    print(10 * C[0], 10 * C[0] + 1, sep='
')
            elif S[0] == 2:
                if C[0] == 0:
                    print(-1)
                else:
                    print(10 + C[0], 10 + C[0], sep='
')
            else:
                print(-1)
        return
    if N == 3:
        if M == 0:
            print(100, 101, 102, 103, 104, 105, 106, 107, 108, 109, sep='
')
        else:
            if S[0] == 1:
                if C[0] == 0:
                    print(-1)
                else:
                    print(100 * C[0], 100 * C[0] + 1, 100 * C[0] + 2, 100 * C[0] + 3, 100 * C[0] + 4, 100 * C[0] + 5, 100 * C[0] + 6, 100 * C[0] + 7, 100 * C[0] + 8, 100 * C[0] + 9, sep='
')
            elif S[0] == 2:
                if C[0] == 0:
                    print(-1)
                else:
                    print(10 + C[0], 10 + C[0], sep='
')
            elif S[0] == 3:
                if C[0]

if __name__ == '__main__':
    main()