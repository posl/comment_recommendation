def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    ans = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if s[j] - s[i] >= k:
                ans += 1
    print(ans)
