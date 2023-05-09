def main():
    n = int(input())
    s = [tuple(map(int, input().split())) for _ in range(n)]
    t = [tuple(map(int, input().split())) for _ in range(n)]
    # まず、sの重心を原点に移動する
    sx = sum([x for x, y in s]) / n
    sy = sum([y for x, y in s]) / n
    s = [(x - sx, y - sy) for x, y in s]
    # 次に、tの重心を原点に移動する
    tx = sum([x for x, y in t]) / n
    ty = sum([y for x, y in t]) / n
    t = [(x - tx, y - ty) for x, y in t]
    # さらに、sの重心とtの重心が一致するように、tを移動する
    t = [(x + sx - tx, y + sy - ty) for x, y in t]
    # sとtの重心が一致するように、tを移動させる
    # このとき、sとtの重心は原点になる
    # sとtが一致するかを判定する
    s = sorted(s)
    t = sorted(t)
    for i in range(n):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()