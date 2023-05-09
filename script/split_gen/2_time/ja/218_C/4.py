def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    def is_same(S, T):
        for i in range(N):
            for j in range(N):
                if S[i][j] != T[i][j]:
                    return False
        return True
    def rotate(S):
        T = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                T[i][j] = S[N - j - 1][i]
        return T
    def flip(S):
        T = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                T[i][j] = S[i][N - j - 1]
        return T
    def is_same_with_flip(S, T):
        return is_same(S, T) or is_same(flip(S), T)
    def is_same_with_rotate(S, T):
        for _ in range(4):
            if is_same(S, T):
                return True
            S = rotate(S)
        return False
    if is_same_with_rotate(S, T) and is_same_with_flip(S, T):
        print('Yes')
    else:
        print('No')
