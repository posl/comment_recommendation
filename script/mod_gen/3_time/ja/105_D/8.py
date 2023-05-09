def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Aの累積和を取る
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = sum_A[i] + A[i]
    # Mで割った余りを取る
    for i in range(N + 1):
        sum_A[i] %= M
    # Mで割った余りが同じ要素同士の組み合わせを数える
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(N + 1):
        d[sum_A[i]] += 1
    # 2つ選ぶ組み合わせを数える
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()