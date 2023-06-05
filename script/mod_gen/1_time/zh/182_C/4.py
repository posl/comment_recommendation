def main():
    n = int(input())
    k = len(str(n))
    if k == 1:
        print(-1)
        return
    if k == 2:
        if n % 3 == 0:
            print(0)
        else:
            print(-1)
        return
    if k == 3:
        if n % 3 == 0:
            print(0)
        elif (n // 10) % 3 == 0 or (n % 100) % 3 == 0:
            print(1)
        else:
            print(-1)
        return
    if k == 4:
        if n % 3 == 0:
            print(0)
        elif (n // 10) % 3 == 0 or (n % 100) % 3 == 0 or (n % 1000) % 3 == 0 or (n % 10000) % 3 == 0:
            print(1)
        else:
            print(-1)
        return
    if k == 5:
        if n % 3 == 0:
            print(0)
        elif (n // 10) % 3 == 0 or (n % 100) % 3 == 0 or (n % 1000) % 3 == 0 or (n % 10000) % 3 == 0 or (n % 100000) % 3 == 0 or (n % 1000000) % 3 == 0:
            print(1)
        else:
            print(-1)
        return
    if k == 6:
        if n % 3 == 0:
            print(0)
        elif (n // 10) % 3 == 0 or (n % 100) % 3 == 0 or (n % 1000) % 3 == 0 or (n % 10000) % 3 == 0 or (n % 100000) % 3 == 0 or (n % 1000000) % 3 == 0 or (n % 10000000) % 3 == 0 or (n % 100000000) % 3 == 0:
            print(1)
        else:
            print(-1)
        return

if __name__ == '__main__':
    main()