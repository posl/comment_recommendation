def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    #print(S,T)
    for i in range(N):
        for j in range(N):
            if S[i][j] != T[i][j]:
                S[i] = S[i][:j] + '#' + S[i][j+1:]
            else:
                S[i] = S[i][:j] + '.' + S[i][j+1:]
    #print(S)
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                S[i] = S[i][:j] + '#' + S[i][j+1:]
                if i < N-1:
                    S[i+1] = S[i+1][:j] + '#' + S[i+1][j+1:]
                if j < N-1:
                    S[i] = S[i][:j+1] + '#' + S[i][j+2:]
                if i < N-1 and j < N-1:
                    S[i+1] = S[i+1][:j+1] + '#' + S[i+1][j+2:]
    #print(S)
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                print('No')
                exit()
    print('Yes')
