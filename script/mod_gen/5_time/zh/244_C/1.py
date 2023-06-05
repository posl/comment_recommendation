def main():
    n = int(input())
    l = 1
    r = 2 * n + 1
    while True:
        print((l + r) // 2)
        a = int(input())
        if a == 0:
            break
        elif a == 1:
            l = (l + r) // 2
        else:
            r = (l + r) // 2

if __name__ == '__main__':
    main()