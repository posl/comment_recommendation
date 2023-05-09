def main():
    n = int(input())
    for i in range(111, 1000, 111):
        if n <= i:
            print(i)
            break

if __name__ == '__main__':
    main()