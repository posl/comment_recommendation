def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    print(S)
    for i in range(H):
        for j in range(W):
            print(S[i][j],end='')
        print()
    print(H,W)
    print(S[0][0])
    print(S[0][1])
    print(S[0][2])
    print(S[0][3])
    print(S[0][4])
    print(S[0][5])
    print(S[1][0])
    print(S[1][1])
    print(S[1][2])
    print(S[1][3])
    print(S[1][4])
    print(S[1][5])
    print(S[2][0])
    print(S[2][1])
    print(S[2][2])
    print(S[2][3])
    print(S[2][4])
    print(S[2][5])
    print(S[3][0])
    print(S[3][1])
    print(S[3][2])
    print(S[3][3])
    print(S[3][4])
    print(S[3][5])

if __name__ == '__main__':
    main()