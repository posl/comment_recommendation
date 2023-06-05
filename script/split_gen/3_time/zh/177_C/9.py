def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = 0
    for i in range(n):
        s -= a[i]
        ans += a[i] * s
    print(ans % (10**9 + 7))
