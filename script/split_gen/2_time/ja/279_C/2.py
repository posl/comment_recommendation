def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    if H % 2 == 0 and W % 2 == 0:
        for i in range(H):
            for j in range(W):
                if S[i][j] != T[i][j]:
                    print("No")
                    return
        print("Yes")
        return
    if H % 2 == 0:
        for i in range(H):
            for j in range(W // 2):
                if S[i][j] != T[i][j] or S[i][W - 1 - j] != T[i][W - 1 - j]:
                    print("No")
                    return
        print("Yes")
        return
    if W % 2 == 0:
        for i in range(H // 2):
            for j in range(W):
                if S[i][j] != T[i][j] or S[H - 1 - i][j] != T[H - 1 - i][j]:
                    print("No")
                    return
        print("Yes")
        return
    S1 = []
    S2 = []
    T1 = []
    T2 = []
    for i in range(H // 2):
        for j in range(W // 2):
            if S[i][j] != T[i][j] or S[i][W - 1 - j] != T[i][W - 1 - j] or S[H - 1 - i][j] != T[H - 1 - i][j] or S[H - 1 - i][W - 1 - j] != T[H - 1 - i][W - 1 - j]:
                print("No")
                return
            S1.append(S[i][j])
            S2.append(S[i][W - 1 - j])
            T1.append(T[i][j])
            T2.append(T[i][W - 1 - j])
    S1.sort()
    S2.sort()
    T1.sort()
    T2.sort()
    if S1 == T1 and S2 == T2:
        print("Yes")
        return
    print("No")
