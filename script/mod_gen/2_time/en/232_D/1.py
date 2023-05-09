def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == '.':
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()