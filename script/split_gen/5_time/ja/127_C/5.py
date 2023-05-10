def main():
    n, m = map(int, input().split())
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        l[a] += 1
        r[b] += 1
    ans = 0
    cnt = 0
    for i in range(1, n + 1):
        cnt += l[i]
        if cnt == m:
            ans += 1
        cnt -= r[i]
    print(ans)
