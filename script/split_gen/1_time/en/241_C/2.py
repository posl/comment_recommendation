def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        for j in range(N):
            if S[i][j] == '.':
                S[i] = S[i][:j] + '#' + S[i][j+1:]
                ans = check(S)
                if ans:
                    print('Yes')
                    return
                for k in range(N):
                    for l in range(N):
                        if S[k][l] == '.':
                            S[k] = S[k][:l] + '#' + S[k][l+1:]
                            ans = check(S)
                            if ans:
                                print('Yes')
                                return
                            S[k] = S[k][:l] + '.' + S[k][l+1:]
                S[i] = S[i][:j] + '.' + S[i][j+1:]
    print('No')
