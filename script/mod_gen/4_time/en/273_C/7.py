def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = sorted(a)
    c = [0] * n
    for i in range(n):
        c[b[i]] = i
    ans = [0] * n
    for i in range(n):
        ans[i] = c[a[i]]
    print(*ans, sep='\n')
solve()

if __name__ == '__main__':
    solve()