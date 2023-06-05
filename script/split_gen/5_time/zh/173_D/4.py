def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a + a
    a.append(0)
    s = sum(a[:n])
    ans = s
    t = s
    for i in range(n):
        t = t + a[i+n] - a[i]
        ans = max(ans, t)
    print(ans)
