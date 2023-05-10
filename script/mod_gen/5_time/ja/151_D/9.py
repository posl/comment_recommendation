def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                ans += 1
    if ans == H * W:
        print(ans - 1)
    else:
        print(ans)
main()

if __name__ == '__main__':
    main()