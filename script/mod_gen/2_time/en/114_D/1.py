def main():
    N = int(input())
    divisors = [0] * (N + 1)
    for i in range(2, N + 1):
        for j in range(i, N + 1, i):
            divisors[j] += 1
    print(divisors.count(75))

if __name__ == '__main__':
    main()