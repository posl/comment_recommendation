def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans += 1
    ans -= 4
    ans += H + W - 2
    print(ans)

if __name__ == '__main__':
    main()