def main():
    # 入力
    N = int(input())
    p = [int(input()) for _ in range(N)]
    # 処理
    p.sort()
    p[-1] = p[-1] // 2
    # 出力
    print(sum(p))

if __name__ == '__main__':
    main()