def main():
    # input
    n, k = map(int, input().split())
    # compute
    # n % k == 0
    if n % k == 0:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()