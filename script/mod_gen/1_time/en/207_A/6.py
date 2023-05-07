def main():
    numbers = input().split()
    numbers = [int(i) for i in numbers]
    numbers.sort()
    print(numbers[1] + numbers[2])

if __name__ == '__main__':
    main()