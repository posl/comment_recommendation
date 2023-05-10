def main():
    N,M = map(int,input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    S.sort()
    T.sort()
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                print(-1)
                exit()
    if N == 1:
        print(S[0])
        exit()
    else:
        if N == 2:
            print(S[0]+S[1])
            exit()
        else:
            if N == 3:
                print(S[0]+S[1]+S[2])
                exit()
            else:
                if N == 4:
                    print(S[0]+S[1]+S[2]+S[3])
                    exit()
                else:
                    if N == 5:
                        print(S[0]+S[1]+S[2]+S[3]+S[4])
                        exit()
                    else:
                        if N == 6:
                            print(S[0]+S[1]+S[2]+S[3]+S[4]+S[5])
                            exit()
                        else:
                            if N == 7:
                                print(S[0]+S[1]+S[2]+S[3]+S[4]+S[5]+S[6])
                                exit()
                            else:
                                if N == 8:
                                    print(S[0]+S[1]+S[2]+S[3]+S[4]+S[5]+S[6]+S[7])
                                    exit()

if __name__ == '__main__':
    main()