def main():
    N, M = map(int, input().split())
    S = []
    C = []
    for i in range(M):
        s, c = map(int, input().split())
        S.append(s)
        C.append(c)
    if N == 1:
        if M == 0:
            print(0)
        else:
            if S[0] == 1:
                print(C[0])
            else:
                print(-1)
    elif N == 2:
        if M == 0:
            print(10, 11, sep='
')
        elif M == 1:
            if S[0] == 1:
                if C[0] == 0:
                    print(-1)
                else:
                    print(C[0], 10 + C[0], sep='
')
            elif S[0] == 2:
                if C[0] == 0:
                    print(10, 11, sep='
')
                else:
                    print(10 + C[0], 11 + C[0], sep='
')
            else:
                print(-1)
        elif M == 2:
            if S[0] == 1:
                if S[1] == 2:
                    if C[0] == 0:
                        if C[1] == 0:
                            print(-1)
                        else:
                            print(10 + C[1], 11 + C[1], sep='
')
                    else:
                        print(10 * C[0] + C[1], 11 * C[0] + C[1], sep='
')
                else:
                    print(-1)
            elif S[0] == 2:
                if S[1] == 1:
                    if C[1] == 0:
                        if C[0] == 0:
                            print(-1)
                        else:
                            print(10 + C[0], 11 + C[0], sep='
')
                    else:
                        print(10 * C[1] + C[0], 11 * C[1] + C[0], sep='
')
                else:
                    print(-1)
            else:
                print(-1)
        else:
            print(-1)
    elif N == 3:
        if M == 0:
            print(100, 101
