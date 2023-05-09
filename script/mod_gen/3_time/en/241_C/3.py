def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                continue
            S[i] = S[i][:j] + '#' + S[i][j+1:]
            for k in range(N):
                for l in range(N):
                    if S[k][l] == '#':
                        continue
                    S[k] = S[k][:l] + '#' + S[k][l+1:]
                    if check(S):
                        print('Yes')
                        return
                    S[k] = S[k][:l] + '.' + S[k][l+1:]
            S[i] = S[i][:j] + '.' + S[i][j+1:]
    print('No')

if __name__ == '__main__':
    main()