def main():
    N = int(input())
    c = list(input())
    R = c.count('R')
    W = c.count('W')
    if R == 0 or W == 0:
        print(0)
    else:
        r = 0
        w = 0
        for i in range(R):
            if c[i] == 'W':
                r += 1
        for i in range(R, N):
            if c[i] == 'R':
                w += 1
        print(min(r, w))

if __name__ == '__main__':
    main()