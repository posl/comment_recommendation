def solve():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    def rotate(S):
        res = []
        for j in range(W):
            tmp = ""
            for i in range(H):
                tmp += S[i][j]
            res.append(tmp)
        return res
    for _ in range(4):
        S = rotate(S)
        if S == T:
            print("Yes")
            return
    print("No")
solve()
