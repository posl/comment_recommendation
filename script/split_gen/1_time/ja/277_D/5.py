def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(2 ** n):
        b = []
        for j in range(n):
            if (i >> j) & 1:
                b.append(a[j])
        b.sort()
        x = 0
        for j in range(len(b)):
            if b[j] != x:
                break
            x += 1
        if x < m:
            ans = min(ans, sum(b) + x)
    print(ans)
