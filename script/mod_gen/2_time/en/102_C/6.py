def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    l = [0] * n
    for i in range(n):
        l[i] = a[i] - (i + 1)
    l.sort()
    m = l[n // 2]
    ans = 0
    for i in range(n):
        ans += abs(l[i] - m)
    print(ans)

if __name__ == '__main__':
    solve()