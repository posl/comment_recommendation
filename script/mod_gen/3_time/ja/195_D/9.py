def solve(n, m, q, wv, x, query):
    # 価値の大きい順にソート
    wv.sort(key=lambda x: x[1], reverse=True)
    # 箱の大きさの小さい順にソート
    x.sort()
    for l, r in query:
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r-1:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r-2:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r-3:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r-4:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r-5:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r-6:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが

if __name__ == '__main__':
    solve()