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
            if S[0] == 1:
                print(C[0])
            else:
                print(-1)
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(10, 11)
        elif M == 1:
            if S[0] == 1:
                print(C[0] * 10 + 1, C[0] * 10 + 2)
            elif S[0] == 2:
                print(C[0] + 10, C[0] + 20)
            else:
                print(-1)
        elif M == 2:
            if S[0] == 1 and S[1] == 2:
                print(C[0] * 10 + C[1], C[0] * 10 + C[1] + 10)
            elif S[0] == 2 and S[1] == 1:
                print(C[0] + C[1] * 10, C[0] + C[1] * 10 + 1)
            else:
                print(-1)
        else:
            print(-1)
    elif N == 3:
        if M == 0:
            print(100, 101, 102)
        elif M == 1:
            if S[0] == 1:
                print(C[0] * 100 + 10, C[0] * 100 + 11, C[0] * 100 + 12)
            elif S[0] == 2:
                print(C[0] * 10 + 100, C[0] * 10 + 101, C[0] * 10 + 102)
            elif S[0] == 3:
                print(C[0] + 100, C[0] + 101, C[0] + 102)
            else:
                print(-1)
        elif M == 2

if __name__ == '__main__':
    main()