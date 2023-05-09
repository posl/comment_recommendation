def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #print(S)
    #print(H, W)
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()