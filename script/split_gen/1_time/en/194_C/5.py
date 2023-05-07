def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(1, n):
        ans += (n - i) * a[i] * a[i]
        ans += i * a[i] * a[i]
    print(ans)
