def solve():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    T = []
    for i in range(H):
        T.append(input())
    if S == T:
        print("Yes")
        return
    for i in range(H-1):
        for j in range(W-1):
            if S[i][j] != T[i][j]:
                if S[i][j] == T[i+1][j+1] and S[i+1][j+1] == T[i][j]:
                    S[i] = S[i][:j] + T[i][j] + S[i][j+1:]
                    S[i+1] = S[i+1][:j+1] + T[i+1][j+1] + S[i+1][j+2:]
                    S[i] = S[i][:j+1] + T[i+1][j] + S[i][j+2:]
                    S[i+1] = S[i+1][:j] + T[i][j+1] + S[i+1][j+1:]
                    if S == T:
                        print("Yes")
                        return
                    else:
                        print("No")
                        return
                else:
                    print("No")
                    return
    print("No")

if __name__ == '__main__':
    solve()