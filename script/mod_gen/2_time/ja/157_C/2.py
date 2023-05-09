def main():
    N, M = map(int, input().split())
    S = []
    C = []
    for i in range(M):
        s, c = map(int, input().split())
        S.append(s)
        C.append(c)
    if M == 0:
        if N == 1:
            print(0)
        else:
            print(10 ** (N - 1))
    else:
        for i in range(10 ** (N - 1), 10 ** N):
            for j in range(M):
                if int(str(i)[S[j] - 1]) != C[j]:
                    break
            else:
                print(i)
                break
        else:
            print(-1)

if __name__ == '__main__':
    main()