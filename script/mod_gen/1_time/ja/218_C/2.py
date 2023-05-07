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
        S2 = [["" for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                S2[j][N-1-i] = S[i][j]
        return S2
    def is_same_4(S, T):
        for _ in range(4):
            if is_same(S, T):
                return True
            S = rotate(S)
        return False
    def is_same_2(S, T):
        for _ in range(2):
            if is_same_4(S, T):
                return True
            S = rotate(S)
        return False
    def is_same_1(S, T):
        if is_same_2(S, T):
            return True
        S = rotate(S)
        return is_same_2(S, T)
    print("Yes" if is_same_1(S, T) else "No")

if __name__ == '__main__':
    main()