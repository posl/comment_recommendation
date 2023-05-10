def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a + a
    t = sum(a[:n])
    ans = t
    for i in range(n):
        t = t + a[n + i] - a[i]
        ans = max(ans, t)
    print(ans)
