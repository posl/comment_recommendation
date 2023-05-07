def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    if H%2==0:
        if W%2==0:
            for i in range(H//2):
                for j in range(W//2):
                    if S[i][j]!=S[H-1-i][j] or S[i][j]!=S[i][W-1-j] or S[i][j]!=S[H-1-i][W-1-j]:
                        print("No")
                        return
                    if T[i][j]!=T[H-1-i][j] or T[i][j]!=T[i][W-1-j] or T[i][j]!=T[H-1-i][W-1-j]:
                        print("No")
                        return
        else:
            for i in range(H//2):
                for j in range(W//2):
                    if S[i][j]!=S[H-1-i][j] or S[i][j]!=S[i][W-1-j] or S[i][j]!=S[H-1-i][W-1-j]:
                        print("No")
                        return
                    if T[i][j]!=T[H-1-i][j] or T[i][j]!=T[i][W-1-j] or T[i][j]!=T[H-1-i][W-1-j]:
                        print("No")
                        return
            for i in range(H//2):
                if S[i][W//2]!=S[H-1-i][W//2] or T[i][W//2]!=T[H-1-i][W//2]:
                    print("No")
                    return
    else:
        if W%2==0:
            for i in range(H//2):
                for j in range(W//2):
                    if S[i][j]!=S[H-1-i][j] or S[i][j]!=S[i][W-1-j] or S[i][j]!=S[H-1-i][W-1-j]:
                        print("No")
                        return
                    if T[i][j]!=T[H-1-i][j] or T[i][j]!=T[i][W-1-j] or T[i][j]!=T[H-1-i][W-1-j]:
                        print("No")
                        return
            for

if __name__ == '__main__':
    main()