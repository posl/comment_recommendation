def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        a[i] = a[i] % m
    s = [0]
    for i in range(n):
        s.append((s[-1] + a[i]) % m)
    from collections import Counter
    c = Counter(s)
    ans = 0
    for k in c:
        ans += c[k] * (c[k] - 1) // 2
    print(ans)
