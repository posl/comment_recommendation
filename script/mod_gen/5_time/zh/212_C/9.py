def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ai = 0
    bi = 0
    ans = 10**9
    while ai < n and bi < m:
        ans = min(ans, abs(a[ai] - b[bi]))
        if a[ai] < b[bi]:
            ai += 1
        else:
            bi += 1
    
    print(ans)

if __name__ == '__main__':
    solve()