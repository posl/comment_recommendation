def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N-5):
        for j in range(N-5):
            if S[i][j] == '.':
                S[i] = S[i][:j] + '#' + S[i][j+1:]
                for k in range(6):
                    if S[i+k][j] == '.':
                        S[i+k] = S[i+k][:j] + '#' + S[i+k][j+1:]
                    if S[i][j+k] == '.':
                        S[i] = S[i][:j+k] + '#' + S[i][j+k+1:]
                    if S[i+k][j+k] == '.':
                        S[i+k] = S[i+k][:j+k] + '#' + S[i+k][j+k+1:]
                    if S[i+k][j+5-k] == '.':
                        S[i+k] = S[i+k][:j+5-k] + '#' + S[i+k][j+5-k+1:]
                for k in range(6):
                    if S[i+k][j] == '.':
                        S[i+k] = S[i+k][:j] + '#' + S[i+k][j+1:]
                    if S[i][j+k] == '.':
                        S[i] = S[i][:j+k] + '#' + S[i][j+k+1:]
                    if S[i+k][j+k] == '.':
                        S[i+k] = S[i+k][:j+k] + '#' + S[i+k][j+k+1:]
                    if S[i+k][j+5-k] == '.':
                        S[i+k] = S[i+k][:j+5-k] + '#' + S[i+k][j+5-k+1:]
                for k in range(6):
                    if S[i+k][j] == '.':
                        S[i+k] = S[i+k][:j] + '#' + S[i+k][j+1:]
                    if S[i][j+k] == '.':
                        S[i] = S[i][:j+k] + '#' + S[i][j+k+1:]
                    if S[i+k][j+k] == '.':
                        S[i+k] = S[i+k][:j+k] + '#' + S[i+k][j+k+1:]
                    if S[i+k][j+5-k

if __name__ == '__main__':
    main()