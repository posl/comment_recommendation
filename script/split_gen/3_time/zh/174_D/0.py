def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    cr = c.count('R', 0, r)
    cw = c.count('W', r, N)
    print(min(cr, cw) + abs(r - w))
