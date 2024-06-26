def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    p.sort()
    for i in range(1, 101):
        if not i in p:
            if abs(x - i) < abs(x - p[0]):
                print(i)
                return
            elif abs(x - i) == abs(x - p[0]):
                print(min(i, p[0]))
                return
            else:
                print(p[0])
                return
    print(p[0])
    return

if __name__ == '__main__':
    main()