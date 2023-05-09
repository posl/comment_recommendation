def main():
    numbers = input().split()
    numbers = [int(i) for i in numbers]
    print(len(set(numbers)))

if __name__ == '__main__':
    main()