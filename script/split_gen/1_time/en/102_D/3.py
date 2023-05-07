def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_sum = sum(a)
    a_cumsum = [0] * (n + 1)
    for i in range(n):
        a_cumsum[i + 1] = a_cumsum[i] + a[i]
    ans = 10 ** 18
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            x = a_cumsum[i + 1]
            y = a_cumsum[j + 1] - a_cumsum[i + 1]
            z = a_cumsum[n] - a_cumsum[j + 1]
            ans = min(ans, max(x, y, z) - min(x, y, z))
    print(ans)
