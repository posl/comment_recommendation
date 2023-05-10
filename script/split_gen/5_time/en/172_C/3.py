def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_sum = [0] * (n + 1)
    b_sum = [0] * (m + 1)
    for i in range(n):
        a_sum[i + 1] = a_sum[i] + a[i]
    for i in range(m):
        b_sum[i + 1] = b_sum[i] + b[i]
    ans = 0
    j = m
    for i in range(n + 1):
        if a_sum[i] > k:
            break
        while a_sum[i] + b_sum[j] > k:
            j -= 1
        ans = max(ans, i + j)
    print(ans)
