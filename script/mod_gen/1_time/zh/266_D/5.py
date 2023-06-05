def solve():
    n = int(input())
    s = []
    for _ in range(n):
        t, x, a = map(int, input().split())
        s.append((t, x, a))
    s.sort()
    ans = 0
    for i in range(n):
        t, x, a = s[i]
        if x == 0:
            ans += a
            continue
        for j in range(i + 1, n):
            t2, x2, a2 = s[j]
            if x2 == x:
                continue
            if x2 == 0:
                ans += a2
            break
    print(ans)

if __name__ == '__main__':
    solve()