def solve():
    n,x = map(int, input().split())
    ans = 0
    for i in range(n):
        a,b = map(int, input().split())
        if a <= x <= b:
            ans += 1
    if ans > 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()