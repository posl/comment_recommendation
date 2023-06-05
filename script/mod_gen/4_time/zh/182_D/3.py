def solve():
    n = int(raw_input())
    a = map(int, raw_input().split())
    ans = 0
    sum = 0
    for i in range(n):
        sum += a[i]
        ans = max(ans, sum)
    print ans

if __name__ == '__main__':
    solve()