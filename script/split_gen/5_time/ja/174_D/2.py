def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    else:
        if c[0] == 'W':
            r = c.count('R', 1)
            w = c.count('W', r)
        else:
            w = c.count('W', 1)
            r = c.count('R', w)
        print(min(r, w))
