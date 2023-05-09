def main():
    x, n, *p = map(int, open(0).read().split())
    if n == 0:
        print(x)
        return
    p = set(p)
    for d in range(101):
        if x - d not in p:
            print(x - d)
            return
        if x + d not in p:
            print(x + d)
            return
main()

if __name__ == '__main__':
    main()