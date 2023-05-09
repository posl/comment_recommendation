def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 机Aの読むのに要する時間の累積和
    a_sum = [0] * (n + 1)
    for i in range(n):
        a_sum[i + 1] = a_sum[i] + a[i]
    # 机Bの読むのに要する時間の累積和
    b_sum = [0] * (m + 1)
    for i in range(m):
        b_sum[i + 1] = b_sum[i] + b[i]
    # 机Aの読むのに要する時間の累積和をk以下になるまで減らす
    ans = 0
    j = m
    for i in range(n + 1):
        if a_sum[i] > k:
            break
        while b_sum[j] > k - a_sum[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

if __name__ == '__main__':
    main()