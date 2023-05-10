def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (n - i - 1)
    for i in range(n):
        ans -= a[i] * i
    print(ans * 2)

if __name__ == '__main__':
    solve()