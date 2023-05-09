def main():
    x = int(input())
    count = 0
    while x >= 500:
        x -= 500
        count += 1000
    while x >= 5:
        x -= 5
        count += 5
    print(count)

if __name__ == '__main__':
    main()