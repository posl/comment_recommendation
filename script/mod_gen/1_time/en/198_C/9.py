def main():
    # input
    r, x, y = map(int, input().split())
    # compute
    if (x ** 2 + y ** 2) // (r ** 2) == 0:
        ans = 2
    else:
        ans = ((x ** 2 + y ** 2) // (r ** 2)) ** (1 / 2)
    # output
    print(ans)

if __name__ == '__main__':
    main()