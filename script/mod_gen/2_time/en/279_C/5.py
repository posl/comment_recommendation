def solve():
    H,W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                S[i] = S[i][:j] + '1' + S[i][j+1:]
                T[i] = T[i][:j] + '1' + T[i][j+1:]
            else:
                S[i] = S[i][:j] + '0' + S[i][j+1:]
                T[i] = T[i][:j] + '0' + T[i][j+1:]
    S.sort()
    T.sort()
    if S == T:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()