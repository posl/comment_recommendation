def main():
    n = int(input())
    if n < 10:
        print(n)
    else:
        print(9 + (n - 9) // 10)

if __name__ == '__main__':
    main()