def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    # 降順にソート
    H.sort(reverse=True)
    # モンスターの体力が 0 以下になるまでの攻撃回数を出力
    print(max(0, sum(H) - K))

if __name__ == '__main__':
    main()