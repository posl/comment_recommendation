def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    T = [list(input()) for _ in range(H)]
    def check():
        s = [0] * 26
        t = [0] * 26
        for i in range(H):
            for j in range(W):
                s[ord(S[i][j]) - 35] += 1
                t[ord(T[i][j]) - 35] += 1
        return s == t
    def rotate():
        s = [[0] * H for _ in range(W)]
        for i in range(H):
            for j in range(W):
                s[j][H - i - 1] = S[i][j]
        return s
    def flip():
        s = [[0] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                s[H - i - 1][j] = S[i][j]
        return s
    if check():
        print("Yes")
        return
    S = rotate()
    if check():
        print("Yes")
        return
    S = rotate()
    if check():
        print("Yes")
        return
    S = rotate()
    if check():
        print("Yes")
        return
    S = flip()
    if check():
        print("Yes")
        return
    S = rotate()
    if check():
        print("Yes")
        return
    S = rotate()
    if check():
        print("Yes")
        return
    S = rotate()
    if check():
        print("Yes")
        return
    print("No")
main()

if __name__ == '__main__':
    main()