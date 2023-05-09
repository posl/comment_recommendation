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
    def rotate(S):
        return [''.join([S[N-1-j][i] for j in range(N)]) for i in range(N)]
    def translate(S, a, b):
        return [''.join([S[i-a][j-b] for j in range(N)]) for i in range(N)]
    for a in range(N):
        for b in range(N):
            if check(translate(rotate(S), a, b), T):
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()