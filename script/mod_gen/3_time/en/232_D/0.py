def main():
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == '.':
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()