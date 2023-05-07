def main():
    N = int(input())
    s = [input() for _ in range(N)]
    # s をソートしたものをリストに格納
    sort_s = ["".join(sorted(s[i])) for i in range(N)]
    # 重複を削除
    sort_s = list(set(sort_s))
    # 重複したものの個数をカウント
    count = [sort_s.count(sort_s[i]) for i in range(len(sort_s))]
    # 重複した文字列の個数の組み合わせをカウント
    ans = 0
    for i in range(len(count)):
        ans += count[i] * (count[i] - 1) // 2
    print(ans)
