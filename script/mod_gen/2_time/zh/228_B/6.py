def solve():
    #import sys
    #f = open('test.txt', 'r')
    #sys.stdin = f
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    ans = 1
    i = x
    while a[i] != x + 1:
        ans += 1
        i = a[i] - 1
    print(ans)

if __name__ == '__main__':
    solve()