def solve():
    n = int(input())
    a = list(map(int, input().split()))
    max_p = 0
    p = 0
    for i in range(n):
        p += a[i]
        max_p = max(max_p, p)
    print(max_p)

if __name__ == '__main__':
    solve()