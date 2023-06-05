def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    def rotate(S):
        return [''.join([S[i][j] for i in range(H)]) for j in range(W)]
    def check(S, T):
        return S == T or rotate(S) == T or rotate(rotate(S)) == T or rotate(rotate(rotate(S))) == T
    print("Yes" if check(S, T) else "No")

if __name__ == '__main__':
    solve()