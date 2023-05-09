def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    total = sum(a)
    for i in range(n):
        total -= a[i]
        ans += a[i] * total
    print(ans % (10**9 + 7))
