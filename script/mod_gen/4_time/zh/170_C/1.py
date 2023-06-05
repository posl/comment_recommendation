def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int, input().split()))
    p.sort()
    if x not in p:
        print(x)
        return
    i = 0
    while True:
        if x - i not in p:
            print(x - i)
            return
        if x + i not in p:
            print(x + i)
            return
        i += 1

if __name__ == '__main__':
    main()