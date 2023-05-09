def move(p, a):
    p = p + a
    if p == 4:
        p = 0
    return p

if __name__ == '__main__':
    move()