def main():
    n, x = map(int, input().split())
    p = [int(x) for x in input().split()]
    print(p.index(x) + 1)

if __name__ == '__main__':
    main()