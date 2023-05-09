def solve():
    s = input()
    n = len(s)
    ans = [0]*n
    l = 0
    r = 0
    for i in range(n):
        if s[i] == 'L':
            r = i
        else:
            l = i
        if s[i] == 'L':
            ans[r] += 1
        else:
            ans[l] += 1
    print(*ans)

if __name__ == '__main__':
    solve()