def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    a_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        a_sum[i] = a_sum[i - 1] + a[i - 1]
    ans = -10**18
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                ans = max(ans, a_sum[i] * p + a_sum[j] * q + a_sum[k] * r)
    if ans < 0:
        print("No")
    else:
        print("Yes")
main()
