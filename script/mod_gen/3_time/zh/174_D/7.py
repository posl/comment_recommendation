def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
    else:
        print(min(r,w))

if __name__ == '__main__':
    main()