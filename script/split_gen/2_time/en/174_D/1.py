def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    if c[0] == 'R':
        x = c.index('W')
        print(x)
    else:
        x = c.rindex('R')
        print(x)
    return
