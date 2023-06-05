def main():
    n = int(input())
    x = 1
    while x <= n:
        if x & n:
            print(x)
        x <<= 1

if __name__ == '__main__':
    main()