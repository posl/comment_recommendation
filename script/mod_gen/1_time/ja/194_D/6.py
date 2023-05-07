def main():
    n = int(input())
    print(0 if n == 2 else 1 + sum([1/i for i in range(2, n)]))

if __name__ == '__main__':
    main()