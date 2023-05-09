def main():
    # input
    N = int(input())
    c = input()
    # compute
    r = c.count('R')
    w = c.count('W')
    # output
    print(min(r, w) + abs(r - w) // 2)

if __name__ == '__main__':
    main()