def solve():
    N = int(input())
    S = []
    for i in range(N):
        s = input()
        if s[0] == '!':
            S.append(s[1:])
        else:
            S.append('!' + s)
    S.sort()
    for i in range(N - 1):
        if S[i][0] == '!' and S[i + 1][0] != '!':
            if S[i][1:] == S[i + 1]:
                print(S[i][1:])
                return
    print('satisfiable')
    return

if __name__ == '__main__':
    solve()