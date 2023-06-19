def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(n + 1)
    ans = 0
    left = 0
    for right in range(k + 1):
        ans += max(0, (a[right] - a[right - 1] - 1) // (a[right] - left))
        left = a[right]
    print(ans)
