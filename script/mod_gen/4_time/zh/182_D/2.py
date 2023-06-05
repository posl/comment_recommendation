def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = 0
    s = 0
    for i in range(n):
        s += a[i]
        x = max(x, s)
    print(x)

if __name__ == '__main__':
    solve()