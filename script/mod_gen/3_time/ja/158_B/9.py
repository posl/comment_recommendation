def main():
    n, a, b = map(int, input().split())
    if a == 0:
        print(0)
        return
    elif b == 0:
        print(n)
        return
    # a+b = 1の時は、n%2回操作するので、n%2*a回青いボールがある
    elif a + b == 1:
        print(n % 2 * a)
        return
    # それ以外は、(n // (a + b)) * a + min(n % (a + b), a)回青いボールがある
    else:
        print((n // (a + b)) * a + min(n % (a + b), a))
        return

if __name__ == '__main__':
    main()