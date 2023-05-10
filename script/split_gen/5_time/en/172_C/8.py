def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #累積和を計算
    a_sum = [0] * (n+1)
    for i in range(n):
        a_sum[i+1] = a_sum[i] + a[i]
    b_sum = [0] * (m+1)
    for i in range(m):
        b_sum[i+1] = b_sum[i] + b[i]
    #累積和の中から、kを超えない最大値を求める
    ans = 0
    b_index = m
    for i in range(n+1):
        if a_sum[i] > k:
            break
        while b_sum[b_index] > k - a_sum[i]:
            b_index -= 1
        ans = max(ans, i + b_index)
    print(ans)
