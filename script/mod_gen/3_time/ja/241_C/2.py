def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 'No'
    for i in range(N):
        for j in range(N):
            if S[i][j] == '.':
                S[i] = S[i][:j] + '#' + S[i][j+1:]
                for k in range(N):
                    for l in range(N):
                        if S[k][l] == '.':
                            S[k] = S[k][:l] + '#' + S[k][l+1:]
                            for m i

if __name__ == '__main__':
    main()