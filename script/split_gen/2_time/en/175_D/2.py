def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        j = i
        s = 0
        l = 0
        while True:
            j = p[j] - 1
            s += c[j]
            l += 1
            if j == i:
                break
        if s <= 0:
            ans = max(ans, max(c))
        else:
            m = k // l
            ans = max(ans, max(c[:i + 1]) + m * s)
            ans = max(ans, max(c[:j + 1]) + (m - 1) * s)
    print(ans)
