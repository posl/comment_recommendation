def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(n):
        sum += a[i]
    if a[m-1] * 4 * m >= sum:
        print('是')
    else:
        print('否')

if __name__ == '__main__':
    solve()