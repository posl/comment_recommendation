def main():
    N = int(input())
    S = [int(x) for x in input().split()]
    S.sort()
    if N == 1:
        print(1)
        exit()
    if N == 2:
        if S[0] == S[1]:
            print(0)
        else:
            print(2)
        exit()
    if N == 3:
        if S[0] == S[1] and S[1] == S[2]:
            print(0)
        elif S[0] == S[1] or S[1] == S[2]:
            print(1)
        else:
            print(3)
        exit()
    if N == 4:
        if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
            print(0)
        elif S[0] == S[1] and S[1] == S[2]:
            print(1)
        elif S[1] == S[2] and S[2] == S[3]:
            print(1)
        elif S[0] == S[1] and S[2] == S[3]:
            print(2)
        else:
            print(2)
        exit()
    if N == 5:
        if S[0] == S[1] and S[1] == S[2] and S[2] == S[3] and S[3] == S[4]:
            print(0)
        elif S[0] == S[1] and S[1] == S[2] and S[3] == S[4]:
            print(1)
        elif S[0] == S[1] and S[2] == S[3] and S[3] == S[4]:
            print(1)
        elif S[0] == S[1] and S[1] == S[2]:
            print(1)
        elif S[1] == S[2] and S[2] == S[3]:
            print(1)
        elif S[2] == S[3] and S[3] == S[4]:
            print(1)
        elif S[0] == S[1] and S[3] == S[4

if __name__ == '__main__':
    main()