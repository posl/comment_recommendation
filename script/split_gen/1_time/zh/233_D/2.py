def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    right = 1
    for left in range(n):
        while right <= n and s[right] - s[left] < k:
            right += 1
        if s[right] - s[left] == k:
            ans += 1
    print(ans)
