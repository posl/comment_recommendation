def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == '.':
                for k in range(N):
                    for l in range(N):
                        if S[k][l] == '.':
                            S[i][j] = '#'
                            S[k][l] = '#'
                            for m in range(N):
                                for n in range(N):
                                    if S[m][n] == '.':
                                        S[m][n] = '#'
                                        if check(S):
                                            print('Yes')
                                            return
                                        S[m][n] = '.'
                            S[k][l] = '.'
                            S[i][j] = '.'
    print('No')
    return

if __name__ == '__main__':
    main()