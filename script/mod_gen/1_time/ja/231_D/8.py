def main():
    # 入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 連結要素の個数を数える
    group = [i for i in range(N+1)]
    size = [1] * (N+1)
    def root(x):
        if group[x] == x:
            return x
        else:
            group[x] = root(group[x])
            return group[x]
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        group[y] = x
        size[x] += size[y]
    for a, b in AB:
        unite(a, b)
    # 出力
    if len(set([root(i) for i in range(1, N+1)])) == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()