def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    def is_match(S, T):
        for i in range(N):
            for j in range(N):
                if S[i][j] != T[i][j]:
                    return False
        return True
    def rotate(S):
        S_rot = [''] * N
        for i in range(N):
            for j in range(N):
                S_rot[j] += S[N - 1 - i][j]
        return S_rot
    for _ in range(4):
        if is_match(S, T):
            print('Yes')
            return
        S = rotate(S)
    print('No')

if __name__ == '__main__':
    main()