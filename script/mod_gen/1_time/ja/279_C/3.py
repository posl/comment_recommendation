def main():
    H, W = map(int, input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    #print(S)
    #print(T)
    for i in range(H):
        for j in range(W):
            if S[i][j] == T[i][j]:
                continue
            else:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()