def main():
    N, C = map(int, input().split())
    abc = [list(map(int, input().split())) for _ in range(N)]
    # 2N個のイベントを作る
    # 2N個のイベントをソートする
    # 2N個のイベントを順番に見ていき、イベントの種類に応じて処理する
    # その都度、支払い金額を計算する
    # その都度、最小支払い金額を更新する
    events = []
    for i in range(N):
        a, b, c = abc[i]
        events.append([a - 1, c])
        events.append([b, -c])
    events.sort()
    ans = 0
    fee = 0
    t = 0
    for x, y in events:
        if x != t:
            ans += min(C, fee) * (x - t)
            t = x
        fee += y
    print(ans)

if __name__ == '__main__':
    main()