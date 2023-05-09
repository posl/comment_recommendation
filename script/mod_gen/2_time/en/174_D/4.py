def main():
    n = int(input())
    c = input()
    w = c.count('W')
    r = c.count('R')
    if w == 0 or r == 0:
        print(0)
    elif w == 1 or r == 1:
        print(1)
    else:
        w1 = c[:w].count('W')
        r1 = c[w:].count('R')
        print(min(w1, r1))

if __name__ == '__main__':
    main()