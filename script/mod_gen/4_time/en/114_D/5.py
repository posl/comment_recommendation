def main():
    n = int(input())
    divisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisors += 1
    if divisors == 75:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()