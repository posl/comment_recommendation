def solve():
    H,W = list(map(int,input().split()))
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]
    S_count = [0]*H
    T_count = [0]*H
    for i in range(H):
        S_count[i] = S[i].count("#")
        T_count[i] = T[i].count("#")
    if S_count != T_count:
        print("No")
        return
    for i in range(H):
        if S[i] != T[i]:
            if S[i][0] == "#":
                S[i] = S[i][::-1]
            if S[i] != T[i]:
                print("No")
                return
    print("Yes")
    return
