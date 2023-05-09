def main():
    # input
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())
    # compute
    # output
    print(xN2 + (x0 - xN2) * (2 ** 0.5))
    print(yN2 + (y0 - yN2) * (2 ** 0.5))

if __name__ == '__main__':
    main()