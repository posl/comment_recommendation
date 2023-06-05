def solve(a,s):
    if a > s:
        return 'No'
    if (s-a) & a == 0:
        return 'Yes'
    return 'No'

if __name__ == '__main__':
    solve()