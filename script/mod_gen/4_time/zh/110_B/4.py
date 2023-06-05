def war_or_peace(N, M, X, Y, x, y):
    if max(x) < min(y) and X < min(y) and max(x) < Y:
        return 'war'
    else:
        return 'peace'

if __name__ == '__main__':
    war_or_peace()