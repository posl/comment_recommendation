def main():
    a, b, k = map(int, input().split())
    divisors = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
    print(divisors[-k])

if __name__ == '__main__':
    main()