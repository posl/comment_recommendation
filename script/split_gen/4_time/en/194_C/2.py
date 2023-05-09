def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += (n - 1) * a[i] ** 2
    for i in range(1, n):
        ans -= 2 * a[i] * sum(a[:i])
    print(ans)
