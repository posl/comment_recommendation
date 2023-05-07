def main():
    n = int(input())
    if n <= 0:
        return 0
    else:
        return fizzbuzz(n)

if __name__ == '__main__':
    main()