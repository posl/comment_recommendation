def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    # aの要素の個数を数える
    cnt = [0] * (n + 1)
    for i in range(n):
        cnt[a[i]] += 1
    # 累積和
    sum_cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        sum_cnt[i] = sum_cnt[i - 1] + cnt[i]
    # クエリに答える
    for i in range(q):
        l, r, x = query[i]
        print(sum_cnt[r] - sum_cnt[l - 1])
