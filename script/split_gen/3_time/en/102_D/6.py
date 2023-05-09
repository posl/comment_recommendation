def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = 10 ** 9
    t = 0
    for i in range(n - 1):
        t += a[i]
        ans = min(ans, abs(s - 2 * t))
    print(ans)
