def main():
    p = int(input())
    n = 1
    sum = 0
    while True:
        if n > 10:
            n = 10
        sum += n * factorial(n)
        if sum >= p:
            sum -= n * factorial(n)
            n -= 1
            break
        n += 1
    while True:
        if sum + factorial(n) <= p:
            sum += factorial(n)
            n += 1
        else:
            break
    print(n)

if __name__ == '__main__':
    main()