def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    T = [list(map(int, input().split())) for _ in range(N)]
    Sx = [s[0] for s in S]
    Sy = [s[1] for s in S]
    Tx = [t[0] for t in T]
    Ty = [t[1] for t in T]
    if N == 1:
        if S == T:
            print("Yes")
        else:
            print("No")
    elif N == 2:
        if S[0][0] == S[1][0]:
            if T[0][0] == T[1][0]:
                if S[0][0] == T[0][0]:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        elif S[0][1] == S[1][1]:
            if T[0][1] == T[1][1]:
                if S[0][1] == T[0][1]:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            if T[0][0] == T[1][0]:
                print("No")
            elif T[0][1] == T[1][1]:
                print("No")
            else:
                if (S[0][1] - S[1][1]) / (S[0][0] - S[1][0]) == (T[0][1] - T[1][1]) / (T[0][0] - T[1][0]):
                    print("Yes")
                else:
                    print("No")
    elif N == 3:
        if S[0][0] == S[1][0] and S[1][0] == S[2][0]:
            if T[0][0] == T[1][0] and T[1][0] == T[2][0]:
                if S[0][0] == T[0][0]:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        elif S[0][1] == S[1][1] and S

if __name__ == '__main__':
    main()