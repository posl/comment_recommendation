def main():
    h = int(input())
    count = 0
    while h > 0:
        count += 1
        h //= 2
    print(2 ** count - 1)

if __name__ == '__main__':
    main()