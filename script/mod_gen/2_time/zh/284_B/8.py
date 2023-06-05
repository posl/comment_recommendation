def main():
    # N = int(input())
    # S = []
    # for i in range(N):
    #     S.append(input())
    # for i in range(N):
    #     print(S[N-i-1])
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.reverse()
    for i in range(N):
        print(S[i])

if __name__ == '__main__':
    main()