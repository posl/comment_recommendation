def main():
    a, b = [int(x) for x in input().split()]
    print(32**(a-b))

if __name__ == '__main__':
    main()