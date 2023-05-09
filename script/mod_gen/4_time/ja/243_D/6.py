def move(x, s):
    if s == 'U':
        return x // 2
    elif s == 'L':
        return x * 2
    elif s == 'R':
        return x * 2 + 1
    else:
        return x

if __name__ == '__main__':
    move()