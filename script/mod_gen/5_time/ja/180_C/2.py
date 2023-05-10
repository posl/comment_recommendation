def main():
    N = int(input())
    divisors = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            divisors.append(i)
            if i != N // i:
                divisors.append(N // i)
        i += 1
    divisors.sort()
    for divisor in divisors:
        print(divisor)

if __name__ == '__main__':
    main()