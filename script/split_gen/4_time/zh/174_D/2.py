def main():
    N = int(input())
    c = input()
    w = c.count('W')
    r = c.count('R')
    if w == 0 or r == 0:
        print(0)
        return
    w1 = 0
    r1 = 0
    for i in range(N):
        if c[i] == 'W':
            w1 += 1
        else:
            r1 += 1
        if w1 == r:
            print(r1)
            return
