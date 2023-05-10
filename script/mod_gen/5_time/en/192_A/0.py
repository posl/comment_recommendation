def main():
    a = int(input())
    if a % 100 == 0:
        print(100)
    else:
        print(100 - a % 100)

if __name__ == '__main__':
    main()