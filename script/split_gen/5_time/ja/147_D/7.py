def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(60):
        x = 0
        for j in range(n):
            if a[j] & (1 << i):
                x += 1
        ans += (x * (n - x) * (1 << i))
        ans %= (10 ** 9 + 7)
    print(ans)
