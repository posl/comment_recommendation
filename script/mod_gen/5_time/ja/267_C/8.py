def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    num = 0
    for i in range(m):
        num += a[i]
    for i in range(m,n):
        num += a[i] * (i+1)
    return num

if __name__ == '__main__':
    solve()