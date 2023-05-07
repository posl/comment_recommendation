def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    if H == 1 or W == 1:
        if S == T:
            print("Yes")
        else:
            print("No")
        return
    for i in range(H-1):
        for j in range(W-1):
            if S[i][j:j+2] == T[i][j:j+2] and S[i+1][j:j+2] == T[i+1][j:j+2]:
                continue
            elif S[i][j:j+2] == T[i+1][j:j+2] and S[i+1][j:j+2] == T[i][j:j+2]:
                continue
            else:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()