def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1 << 30
    for i in range(1 << (n - 1)):
        x = 0
        y = 0
        for j in range(n):
            y |= a[j]
            if (i >> j) & 1 or j == n - 1:
                x ^= y
                y = 0
        ans = min(ans, x)
    print(ans)
