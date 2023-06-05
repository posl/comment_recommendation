def solve():
    n,m = map(int,input().split())
    a = [0 for _ in range(n+1)]
    for _ in range(m):
        l,r = map(int,input().split())
        a[l-1] += 1
        a[r] -= 1
    for i in range(n):
        a[i+1] += a[i]
    print(a.count(m))

if __name__ == '__main__':
    solve()