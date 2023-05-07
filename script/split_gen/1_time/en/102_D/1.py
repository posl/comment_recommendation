def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0 for _ in range(n+1)]
    for i in range(n):
        s[i+1] = s[i] + a[i]
    ans = float('inf')
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            ans = min(ans, abs(s[i] - s[0] - s[j] + s[i]), abs(s[i] - s[0] - s[j] + s[j] - s[i]), abs(s[i] - s[0] - s[j] + s[j] - s[i] - s[j] + s[n]))
    print(ans)
