def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    a.append(n + 1)
    for i in range(k):
        ans += max(0, a[i + 1] - a[i] - 1)
    print(n - ans)
