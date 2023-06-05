def main():
    n = int(input())
    c = list(input())
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
        return
    if c[0] == 'R':
        print(w)
    else:
        print(r)
