def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 10**9
    j = 0
    for i in range(n):
        while j < m - 1 and abs(a[i] - b[j]) > abs(a[i] - b[j+1]):
            j += 1
        ans = min(ans, abs(a[i] - b[j]))
    print(ans)

if __name__ == '__main__':
    solve()