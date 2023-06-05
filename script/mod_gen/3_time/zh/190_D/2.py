def main():
    n = int(input())
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i % 2 == 1:
                count += 1
            if i != n // i and (n // i) % 2 == 1:
                count += 1
    print(count)

if __name__ == '__main__':
    main()