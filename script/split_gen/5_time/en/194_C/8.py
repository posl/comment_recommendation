def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += (i * a[i]**2 - 2 * a[i] * sum(a[:i]) + sum(a[:i]) ** 2)
    print(ans)
