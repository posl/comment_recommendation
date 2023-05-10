def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 割引券を使わない場合を初期値とする
    ans = sum(a)
    # 割引券を使う場合を考える
    # 割引券を使う場合は、割引券を使う品物の中で最も安いものを割引券で買うのが最適
    # 割引券を使う品物を全て試す
    for i in range(m):
        a.sort()
        a[0] = a[0] // 2
    print(sum(a))
