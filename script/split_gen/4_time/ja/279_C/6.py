def solve():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S = sorted(S)
    T = sorted(T)
    for i in range(H):
        if S[i] != T[i]:
            print("No")
            return
    print("Yes")
    return
