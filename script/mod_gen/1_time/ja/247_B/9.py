def main():
    # 入力
    N = int(input())
    names = [input().split() for _ in range(N)]
    # 出力
    print('Yes' if solve(N, names) else 'No')

if __name__ == '__main__':
    main()