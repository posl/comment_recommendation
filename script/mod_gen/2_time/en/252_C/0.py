def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 10**10
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        if N == 2:
                            ans = min(ans, abs(int(S[0][i])-int(S[1][j]))+1)
                        elif N == 3:
                            ans = min(ans, abs(int(S[0][i])-int(S[1][j]))+abs(int(S[1][j])-int(S[2][k]))+2)
                        elif N == 4:
                            ans = min(ans, abs(int(S[0][i])-int(S[1][j]))+abs(int(S[1][j])-int(S[2][k]))+abs(int(S[2][k])-int(S[3][l]))+3)
                        elif N == 5:
                            ans = min(ans, abs(int(S[0][i])-int(S[1][j]))+abs(int(S[1][j])-int(S[2][k]))+abs(int(S[2][k])-int(S[3][l]))+abs(int(S[3][l])-int(S[4][m]))+4)
    print(ans)

if __name__ == '__main__':
    main()