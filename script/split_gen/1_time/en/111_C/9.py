def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = n
    for i in range(2):
        b = a[i::2]
        c = a[1-i::2]
        d = sorted(b + c)
        e = d[0]
        f = d[-1]
        if e != f:
            ans = min(ans, b.count(e) + c.count(f))
    print(ans)
