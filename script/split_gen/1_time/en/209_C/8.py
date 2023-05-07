def main():
    N = int(input())
    C = list(map(int, input().split()))
    mod = 10**9 + 7
    # 配列Cの最大値を求める
    max_C = max(C)
    # Cの要素の個数を数える
    C_count = [0] * (max_C + 1)
    for c in C:
        C_count[c] += 1
    # 2つ以上ある要素の個数を数える
    C_2more = 0
    for c in C_count:
        if c >= 2:
            C_2more += 1
    # 2つ以上ある要素がある場合は0
    if C_2more >= 2:
        print(0)
        return
    # 2つ以上ある要素がない場合は、Cの要素の個数を数える
    ans = 1
    for c in C_count:
        if c >= 1:
            ans = ans * c % mod
    print(ans)
