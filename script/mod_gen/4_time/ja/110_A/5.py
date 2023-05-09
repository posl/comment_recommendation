def main():
    # input
    a, b, c = map(int, input().split())
    # compute
    # output
    print(max(a + b + c, a + b - c, a - b + c, -a + b + c))

if __name__ == '__main__':
    main()