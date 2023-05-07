def main():
    n = int(input())
    a = n // 2
    if n % 2 == 0:
        print(a / n)
    else:
        print((a + 1) / n)

if __name__ == '__main__':
    main()