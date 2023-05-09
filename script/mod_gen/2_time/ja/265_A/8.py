def main():
    # 入力
    X, Y, N = map(int, input().split())
    # 処理
    # 1個のりんごを買うときの最小金額を求める
    min_cost = min(X, Y)
    # 3個のりんごを買うときの最小金額を求める
    min_cost3 = min(X*3, Y)
    # 3個のりんごを買うときの最小金額から1個のりんごを買うときの最小金額を引く
    min_cost1 = min_cost3 - min_cost
    # 3個のりんごを買うときの最小金額から1個のりんごを買うときの最小金額を引く
    min_cost2 = min_cost3 - min_cost
    # 3個のりんごを買うときの最小金額から1個のりんごを買うときの最小金額を引く
    min_cost3 = min_cost3 - min_cost
    # 3個のりん

if __name__ == '__main__':
    main()