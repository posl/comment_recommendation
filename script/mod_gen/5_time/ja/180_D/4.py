def main():
    # input
    x, y, a, b = map(int, input().split())
    # compute
    exp = 0
    while x*a < x+b and x*a < y:
        x *= a
        exp += 1
    exp += (y-x-1)//b
    # output
    print(exp)

if __name__ == '__main__':
    main()