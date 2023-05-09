def main():
    n, m = map(int, input().split())
    l = [0] * (m + 1)
    r = [0] * (m + 1)
    for i in range(1, m + 1):
        l[i], r[i] = map(int, input().split())
    l = sorted(l)
    r = sorted(r)
    ans = 0
    for i in range(1, m + 1):
        ans += max(0, l[i] - r[i - 1])
    print(ans)
