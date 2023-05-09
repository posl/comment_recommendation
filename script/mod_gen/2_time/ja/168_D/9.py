def solve(n, m, a, b):
    # 部屋の数だけ、道しるべの先を格納する配列を用意
    ans = [0] * n
    # 部屋の数だけ、部屋に繋がっている道しるべの数を格納する配列を用意
    cnt = [0] * n
    # 部屋の数だけ、部屋に繋がっている道しるべの先を格納する配列を用意
    # 2次元配列にする
    to = [[] for _ in range(n)]
    # 部屋の数だけ、部屋に繋がっている道しるべの先を格納する配列を用意
    # 2次元配列にする
    from_ = [[] for _ in range(n)]
    # 部屋に繋がっている道しるべの数をカウント
    for i in range(m):
        cnt[a[i] - 1] += 1
        cnt[b[i] - 1] += 1
    # 部屋に繋がっている道しるべの先を格納
    for i in range(m):
        to[a[i] - 1].append(b[i] - 1)
        to[b[i] - 1].append(a[i] - 1)
    # 部屋に繋がっている道しるべの先を格納
    for i in range(m):
        from_[b[i] - 1].append(a[i] - 1)
        from_[a[i] - 1].append(b[i] - 1)
    # 部屋に繋がっている道しるべの数が2つでない場合は、Noを出力
    for i in range(n):
        if cnt[i] != 2:
            print('No')
            return
    # 部屋に繋がっている道しる

if __name__ == '__main__':
    solve()