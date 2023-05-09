def main():
    numbers = [int(x) for x in input().split()]
    numbers.sort()
    print((numbers[0] + numbers[1]) * 10 + numbers[2])

if __name__ == '__main__':
    main()