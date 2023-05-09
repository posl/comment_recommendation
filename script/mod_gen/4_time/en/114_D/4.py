def main():
    N = int(input())
    divisors = [1]
    for i in range(2, N + 1):
        for j in range(len(divisors)):
            divisors.append(divisors[j] * i)
    divisors.sort()
    print(divisors.count(divisors[-1]))

if __name__ == '__main__':
    main()