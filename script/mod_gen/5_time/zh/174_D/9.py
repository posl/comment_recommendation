def min_swap(s):
    n = len(s)
    r = 0
    w = 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
        else:
            w += 1
    if r == 0 or w == 0:
        return 0
    if s[0] == 'R':
        r -= 1
    else:
        w -= 1
    if s[-1] == 'R':
        r -= 1
    else:
        w -= 1
    return min(r, w) + 1

if __name__ == '__main__':
    min_swap()