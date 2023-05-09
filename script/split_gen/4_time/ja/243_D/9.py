def move(n, s, x):
    if n == 0:
        return x
    if s[n-1] == 'U':
        return move(n-1, s, x//2)
    elif s[n-1] == 'L':
        return move(n-1, s, x//2)
    else:
        return move(n-1, s, x//2+1)
