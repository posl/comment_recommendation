def main():
    a, n = map(int, input().split())
    #a = 2
    #n = 767090
    count = 0
    while n > 1:
        if n % a != 0:
            if n % 10 == 0:
                break
            else:
                n = int(str(n)[-1] + str(n)[:-1])
                count += 1
        else:
            n = n // a
            count += 1
    if n == 1:
        print(count)
    else:
        print(-1)

if __name__ == '__main__':
    main()