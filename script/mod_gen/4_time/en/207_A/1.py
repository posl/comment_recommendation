def main():
    # input
    a, b, c = map(int, input().split())
    # compute
    # output
    print(max(a+b, b+c, c+a))

if __name__ == '__main__':
    main()