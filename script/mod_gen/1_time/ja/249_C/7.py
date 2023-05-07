def solve():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    # すべての文字列の集合を作る
    all_str = set()
    for s in S:
        for c in s:
            all_str.add(c)
    # 選ぶ文字列の集合を作る
    choose_str = set()
    for s in S:
        if len(s) < K:
            continue
        for c in s:
            choose_str.add(c)
    # 選ぶ文字列の集合からすべての文字列の集合を引く
    diff = all_str - choose_str
    # 選ばない文字列の集合からすべての文字列の集合を引く
    diff2 = all_str - diff
    # 選ぶ文字列の集合から選ばない文字列の集合を引く
    diff3 = choose_str - diff2
    # 選ぶ文字列の集合から選ばない文字列の集合を引く
    diff4 = choose_str - diff3
    # 選ぶ文字列の集合から選ばない文字列の集合を引く
    diff5 = choose_str - diff4
    # 選ぶ文字列の集合から選ばない文字列の集合を引く
    diff6 = choose_str - diff5
    # 選ぶ文字列の集合から選

if __name__ == '__main__':
    solve()