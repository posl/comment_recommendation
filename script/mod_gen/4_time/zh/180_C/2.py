def main():
    n = int(input())
    result = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    result.sort()
    for i in result:
        print(i)

if __name__ == '__main__':
    main()