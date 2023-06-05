def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, a[i + k - 1] - a[i])
    print(ans + 1)
