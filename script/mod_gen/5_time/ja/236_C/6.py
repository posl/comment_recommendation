def solve():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    i = 0
    j = 0
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == m:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()