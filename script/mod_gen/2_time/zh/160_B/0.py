def main():
    X = int(input())
    count = 0
    while X >= 500:
        count += 1000
        X -= 500
    while X >= 5:
        count += 5
        X -= 5
    print(count)

if __name__ == '__main__':
    main()