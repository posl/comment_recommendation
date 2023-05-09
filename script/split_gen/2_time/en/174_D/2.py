def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    if c[0] == 'R':
        r -= 1
    else:
        w -= 1
    if c[-1] == 'W':
        w -= 1
    else:
        r -= 1
    print(min(r, w))
