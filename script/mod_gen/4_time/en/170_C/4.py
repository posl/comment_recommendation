def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    for i in range(0, 100):
        if not x - i in p:
            print(x - i)
            return
        if not x + i in p:
            print(x + i)
            return

if __name__ == '__main__':
    main()