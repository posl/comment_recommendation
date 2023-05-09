def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    for i in range(W):
        cnt = 0
        for j in range(H):
            if C[j][i] == '#':
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()