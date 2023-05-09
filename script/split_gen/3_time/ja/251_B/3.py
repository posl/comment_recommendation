def main():
    n,w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(2**n):
        s = 0
        for j in range(n):
            if (i >> j) & 1:
                s += a[j]
        if s <= w:
            ans += 1
    print(ans)
