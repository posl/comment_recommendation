def solve(a, s):
    if a > s:
        return 'No'
    elif (s - a) % 2 == 0:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    solve()