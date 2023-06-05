def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum_a = [0] * (n + 1)
    sum_b = [0] * (m + 1)
    for i in range(n):
        sum_a[i + 1] = sum_a[i] + a[i]
    for i in range(m):
        sum_b[i + 1] = sum_b[i] + b[i]
    ans = 0
    j = m
    for i in range(n + 1):
        if sum_a[i] > k:
            break
        while sum_b[j] > k - sum_a[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)
