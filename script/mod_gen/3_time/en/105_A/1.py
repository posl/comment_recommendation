def main():
    n, k = [int(x) for x in input().split()]
    if n % k == 0:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()