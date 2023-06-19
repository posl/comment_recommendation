def solve():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = 0
    for i in range(n):
        ans += a[i] * i + b[i] * (n - i)
    print(ans)

if __name__ == '__main__':
    solve()