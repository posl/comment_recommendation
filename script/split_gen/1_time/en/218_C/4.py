def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    def check(S, T):
        for i in range(N):
            for j in range(N):
                if S[i][j] != T[i][j]:
                    return False
        return True
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#' and T[i][j] == '#':
                for k in range(4):
                    if check(S, T):
                        print('Yes')
                        return
                    T = [''.join(T[i][j] for i in range(N))[::-1] for j in range(N)]
            elif S[i][j] == '#' and T[i][j] == '.':
                for k in range(4):
                    if check(S, T):
                        print('Yes')
                        return
                    T = [''.join(T[i][j] for i in range(N))[::-1] for j in range(N)]
    print('No')
    return
main()
