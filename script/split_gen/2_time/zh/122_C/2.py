def solve(s, l, r):
    count = 0
    for i in range(l-1, r):
        if s[i:i+2] == 'AC':
            count += 1
    return count
