def main():
    n = int(input())
    divisors = [0] * (n+1)
    for i in range(2, n+1):
        for j in range(2, n+1):
            while i % j == 0:
                divisors[j] += 1
                i /= j
    c = 0
    for i in divisors:
        if i >= 74:
            c += 1
    for i in divisors:
        if i >= 24:
            c += (c-1)
    for i in divisors:
        if i >= 14:
            c += (c-1)
    for i in divisors:
        if i >= 4:
            c += (c-1)
    for i in divisors:
        if i >= 2:
            c += (c-1)
    print(c)

if __name__ == '__main__':
    main()