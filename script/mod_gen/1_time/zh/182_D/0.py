def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    s = 0
    for i in range(n):
        x += a[i]
        s = max(s, x)
    print(s)

if __name__ == '__main__':
    solve()