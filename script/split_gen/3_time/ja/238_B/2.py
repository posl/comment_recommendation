def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i]
    ans = 360 * (n - 2) - ans
    print(ans)
