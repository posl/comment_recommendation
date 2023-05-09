def solve(a, s):
    if a > s:
        return 'No'
    if a == s:
        return 'Yes'
    if s % 2 == 1:
        return 'No'
    x = s // 2
    if a < x:
        return 'No'
    return 'Yes'

if __name__ == '__main__':
    solve()