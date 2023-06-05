def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        ans += a[i]
        a[i] = ans
    print(max(a))

if __name__ == '__main__':
    solve()