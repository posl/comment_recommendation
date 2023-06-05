def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if m > n:
        return 'No'
    a.sort()
    b.sort()
    for i in range(m):
        if a[n-m+i] < b[i]:
            return 'No'
    return 'Yes'

if __name__ == '__main__':
    solve()