def main():
    # 入力
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    # 出力
    for j in range(W):
        print(sum(1 for i in range(H) if C[i][j] == '#'), end=' ')
    print()

if __name__ == '__main__':
    main()