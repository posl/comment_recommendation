def main():
    a, b = map(int, input().split())
    sum = a + b
    diff = a - b
    prod = a * b
    print(max(sum, diff, prod))

if __name__ == '__main__':
    main()