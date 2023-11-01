def fight(a,b,c,d):
    while True:
        c -= b
        if c <= 0:
            return True
        a -= d
        if a <= 0:
            return False

if __name__ == '__main__':
    fight()