def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        s = a[i]
        for j in range(i+1, n):
            s += a[j]
            if j - i + 1 == m:
                ans = max(ans, s)
    print(ans)
