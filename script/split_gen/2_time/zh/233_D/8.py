def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    right = 0
    for left in range(n):
        while right < n and s[right + 1] - s[left] < k:
            right += 1
        if s[right + 1] - s[left] == k:
            ans += 1
    print(ans)
