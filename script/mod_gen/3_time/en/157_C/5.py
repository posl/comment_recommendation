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
        elif M == 1:
            print(C[0])
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(10)
        elif M == 1:
            if S[0] == 1:
                if C[0] == 0:
                    print(-1)
                else:
                    print(C[0]*10)
            else:
                print(C[0]*10 + 1)
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                if C[0] == 0:
                    print(-1)
                else:
                    print(C[0]*10 + C[1])
            else:
                print(-1)
        else:
            print(-1)
    else:
        if M == 0:
            print(100)
        elif M == 1:
            if S[0] == 1:
                if C[0] == 0:
                    print(-1)
                else:
                    print(C[0]*100)
            elif S[0] == 2:
                print(C[0]*10 + 10)
            else:
                print(C[0]*100 + 1)
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                if C[0] == 0:
                    print(-1)
                else:
                    print(C[0]*100 + C[1]*10)
            elif S[0] == 1 and S[1] == 3:
                if C[0] == 0:
                    print(-1)
                else:
                    print(C[0]*100 + C[1])
            elif S[0] == 2 and S[1] == 3:
                print(C[0]*10 + C[1] + 10)
            else:
                print(-1)
        elif M == 3:
            if S[0] == 1 and S[1] ==

if __name__ == '__main__':
    main()